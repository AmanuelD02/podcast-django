from django.urls import path
from .views import PostPodcastView, PodcastView

urlpatterns = [
    path('<int:user_id>/channels/<int:channel_id>/audios/', PostPodcastView.as_view()),
    path('<int:user_id>/channels/<int:channel_id>/audios/<int:id>', PodcastView.as_view())
]