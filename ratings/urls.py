from django.urls import path
from .views import PostRatingView,RatingView,RatingsView

urlpatterns = [
    path('',PostRatingView.as_view()),
    path('<int:id>/',RatingView.as_view()),
    path('<int:channel_id>',RatingsView.as_view())
]