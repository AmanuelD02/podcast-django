from cgi import print_form
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters

from recommendations.recommend import RecommenderFactory



from .models import Channel, Subscribe
from .serializers import ChannelSerializer, SubscribeSerializer

# Create your views here.

class ChannelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields  = ['channel_name','description']

    

    def get_serializer_context(self):
        return {'request':self.request}

    @action( detail=False, methods=['get'])
    def my_channels(self,request,pk=None):
        owner = self.request.user

        result = Channel.objects.filter(user_id=owner)
        serializer = ChannelSerializer(result, many=True)
        print(len(serializer.data))
        return Response(serializer.data)
    

    @action(detail= False, methods=['get'])
    def top_rated(self, request):
        recommender = RecommenderFactory().recommender
        channel_ids = list(recommender.recommend(1))
        channels = Channel.objects.filter(id__in=channel_ids)

        serializer = ChannelSerializer(channels, many=True)

        return Response(serializer.data)

    @action(detail= False, methods=['get'])
    def all_channels(self, request):
        channels = Channel.objects.all()

        serializer = ChannelSerializer(channels, many=True)

        return Response(serializer.data)
    



class SubscriptionViewSet(ModelViewSet):
    
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        return Subscribe.objects.filter(user_id=self.request.user)
    def get_serializer_context(self):
        return {'request':self.request}
        




        