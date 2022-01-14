from django.urls import path
from .views import IsRatedView, PostRatingView,RatingView,RatingsView

urlpatterns = [
    path('',PostRatingView.as_view()),
    path('<str:channel_id>/<int:user_id>/',RatingView.as_view()),
    path('channel/<str:channel_id>/',RatingsView.as_view()),
    path('isRated/<str:channel_id>/<int:user_id>/',IsRatedView.as_view())
]