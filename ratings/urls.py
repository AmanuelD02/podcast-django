from django.urls import path
from .views import RatingView

urlpatterns = [
    path('<int:channel_id>/rating/',RatingView.as_view())
]