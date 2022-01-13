from django.urls import path
from .views import DownloadPodcastView, PostPodcastView, PodcastView

urlpatterns = [
    path('', PostPodcastView.as_view()),
    path('<str:id>/', PodcastView.as_view()),
    path('<str:id>/download', DownloadPodcastView.as_view())

]