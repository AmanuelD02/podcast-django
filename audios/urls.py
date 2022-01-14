from django.urls import path
from .views import DownloadPodcastView, PodcastsView, PostPodcastView, PodcastView, GetRecentlyView

urlpatterns = [
    path('recently/', GetRecentlyView.as_view()),
    path('<str:id>/download', DownloadPodcastView.as_view()),
    path('<str:id>/', PodcastView.as_view()),
    path('', PostPodcastView.as_view()),
    path('channel/<str:channel_id>/', PodcastsView.as_view())

]