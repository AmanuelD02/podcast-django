from django.urls import path
from .views import EditProfile, LoginView, RegisterView, LoginSerializer, TestView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('test/', TestView.as_view()),
    path('edit/<int:id>/',EditProfile.as_view()),
]