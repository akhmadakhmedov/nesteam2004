from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import UserSerializer

def users_list(request):
    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

def user_detail(request, pk):
    detail = User.objects.get(pk=pk)
    serializer = UserSerializer(detail)
    data = serializer.data
    return JsonResponse(data, safe=False)

