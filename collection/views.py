from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serialzers import GameCollectionSerializer
from .models import GameCollection

class CollectionViewSet(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = GameCollectionSerializer