from django.urls import path
from .views import DownloadPodcastView, PostPodcastView, PodcastView

urlpatterns = [
    path('<int:user_id>/channels/<int:channel_id>/audios/', PostPodcastView.as_view()),
    path('<int:user_id>/channels/<int:channel_id>/audios/<int:id>', PodcastView.as_view()),
    path('<int:id>/download', DownloadPodcastView.as_view())

]