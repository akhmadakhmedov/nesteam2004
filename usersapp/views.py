from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .filters import PlayerFilter

def users_list(request):
    user_list = User.objects.all()
    serializer = UserListSerializer(user_list, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

def user_detail(request, pk):
    detail = User.objects.get(pk=pk)
    serializer = UserListSerializer(detail)
    data = serializer.data
    return JsonResponse(data, safe=False)

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)

class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filterset_class = PlayerFilter


