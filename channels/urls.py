from django.urls import path
from rest_framework import views
from rest_framework import routers
from . import views 

from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('subscribe',views.SubscriptionViewSet,basename="subscribe")
router.register('',views.ChannelViewSet)


urlpatterns = router.urls