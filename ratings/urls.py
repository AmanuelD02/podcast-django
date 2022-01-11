from django.urls import path
from .views import PostRatingView,RatingView

urlpatterns = [
    path('',PostRatingView.as_view()),
    path('<int:id>',RatingView.as_view())
]