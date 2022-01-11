from django.urls import path
from .views import PostRatingView

urlpatterns = [
    path('user/channel/rating/',PostRatingView.as_view())
]