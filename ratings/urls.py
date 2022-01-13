from django.urls import path
from .views import PostRatingView,RatingView,RatingsView

urlpatterns = [
    path('',PostRatingView.as_view()),
    path('<str:id>/',RatingView.as_view()),
    path('channel/<str:channel_id>/',RatingsView.as_view())
]