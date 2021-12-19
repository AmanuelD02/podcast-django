from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters



from .models import Channel, Subscribe
from .serializers import ChannelSerializer, SubscribeSerializer

# Create your views here.

class ChannelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields  = ['channel_name','description']

    

    def get_serializer_context(self):
        return {'request':self.request}

    @action( detail=False, methods=['get'])
    def my_channels(self,request,pk=None):
        owner = self.request.user

        result = Channel.objects.filter(user_id=owner)
        serializer = ChannelSerializer(result, many=True)
        return Response(serializer.data)



class SubscriptionViewSet(ModelViewSet):
    
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        return Subscribe.objects.filter(user_id=self.request.user)
    def get_serializer_context(self):
        return {'request':self.request}

