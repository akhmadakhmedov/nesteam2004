from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet


#def games_list(request):
#    game_lst = Game.objects.all()
#    serializer = GameSerializer(game_lst, many=True)
#    data = serializer.data
#    return JsonResponse(data, safe=False)


#class CreateGameAPIView(CreateAPIView):
#    serializer_class = GameSerializer
#    queryset = Game.objects.all()

#class GamesListAPIView(ListAPIView):
#    queryset = Game.objects.all()
#    serializer_class = GameSerializer

class GamesView(ListCreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

#def studio(request):
#    studio_list = Studio.objects.all()
#    serializer = StudioSerializer(studio_list, many=True)
#    data = serializer.data
#    return JsonResponse(data, safe=False)

class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class StudiosCreateAPIView(CreateAPIView):
    serializer_class = StudioSerializer
    queryset = Studio.objects.all()

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
