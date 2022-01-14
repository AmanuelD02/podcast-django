import pickle
import os 
import time

import sqlite3
import numpy as np
import pandas as pd
from lightfm import LightFM
from lightfm.data import Dataset
from lightfm.cross_validation import random_train_test_split

from abc import ABC, abstractmethod


PICKLE_FILE_PATH = "recommender.model"




class TrainingStrategy(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.model = LightFM(loss='warp', no_components=4)
    @abstractmethod
    def fit_model(self, dataset, interactions, item_features):
        pass

    @abstractmethod
    def post_process(self, model):
        pass    
    

class RecommenderModelTraining(TrainingStrategy):
    def fit_model(self, dataset, interactions, item_features):
        self.model = LightFM(loss='warp', no_components=4)
        self.model.fit(interactions, item_features=item_features, num_threads=4)
    
    def post_process(self, trainer):
        with open(PICKLE_FILE_PATH, "wb") as f:
            pickle.dump([self.model, time.time(), trainer], f)
        

class AccuracyTestModelTraining:
    def fit_model(self, dataset, interactions, item_features):
        self.item_features = item_features
        self.train, self.test = random_train_test_split(interactions)
        self.model = LightFM(loss='warp', no_components=4)
        self.model.fit(self.train, item_features=item_features, num_threads=4)
        return self.model

    def post_process(self):
        from lightfm.evaluation import recall_at_k
        print("Train recall: %.4f" % recall_at_k(self.model, self.train, item_features=self.item_features, num_threads=4, k=100).mean())
        print("Test recall: %.4f" % recall_at_k(self.model, self.test, item_features=self.item_features, num_threads=4, k=100).mean())
        pass

class Trainer:
    def __init__(self):
        self.dataset = Dataset()
    def get_data(self):
        from pathlib import Path
        BASE_DIR = Path(__file__).resolve().parent.parent
        conn_string = str(BASE_DIR) + '/db.sqlite3'
        print(f'{conn_string=}')
        conn = sqlite3.connect(conn_string)
        data = pd.read_sql("""SELECT rating, ratings_rating.user_id_id as author_id, channel_id_id as podcast_id, subscriber
                                FROM ratings_rating 
                                INNER JOIN channels_channel on ratings_rating.channel_id_id = channels_channel.id
                            """, 
                        conn)
        print(data)
        conn.close()
        return data

    def train_model(self, trainer: TrainingStrategy):
        self.data = self.get_data()
        self.dataset.fit(self.data['author_id'], self.data['podcast_id'])
        self.dataset.fit_partial(items=self.data['podcast_id'],
                    item_features=self.data['subscriber'])
        self.num_users, self.num_items = self.dataset.interactions_shape()
        (interactions, _) = self.dataset.build_interactions(zip(self.data['author_id'], self.data['podcast_id'], self.data['rating']))
        item_features = self.dataset.build_item_features(map(lambda x: (x[0][1], [x[1]]), 
                                                    zip(self.data['podcast_id'].items(), self.data['subscriber'])))

        trainer.fit_model(self.dataset, interactions, item_features)
        trainer.post_process(self)
        return trainer.model


class Recommender:
    def __init__(self):
        # try: 
        #     with open(PICKLE_FILE_PATH, "rb") as f:
        #         self.model, self.time, self.trainer = pickle.load(f)
        # except Exception:
        #     self.model = self.time = None
        self.model = self.time = None
        self.get_model()
    
    def get_model(self):
        if self.model == None or time.time() - self.time > 3600 * 2:
            self.trainer = Trainer()
            self.model = self.trainer.train_model(RecommenderModelTraining())
        return self.model
    def get_dataset(self):
        if self.model == None:
            self.get_model()
        return self.trainer.dataset
    def get_data(self):
        if self.model == None:
            self.get_model()
        return self.trainer.data

    def recommend(self, user_id):
        dataset = self.get_dataset()
        n_items = len(self.model.get_item_representations())
        dataset
        scores = self.model.predict(0, np.arange(n_items))
        data = self.get_data()
        return data['podcast_id'][np.argsort(-scores)][:6]
        
        
    def rating_added(self, user, item, rating):
        dataset = self.get_dataset()
        dataset.fit_partial(users = [user], items=[item])
        new_interactions, new_weights = dataset.build_interactions((user, item, rating))
        model = self.get_model()
        model.fit_partial(new_interactions)
        
        

    def performance_check(self):
        self.trainer.train_model(AccuracyTestModelTraining())

class RecommenderFactory:
    recommender = Recommender()