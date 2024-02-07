from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView


#def games_list(request):
#    game_lst = Game.objects.all()
#    serializer = GameSerializer(game_lst, many=True)
#    data = serializer.data
#    return JsonResponse(data, safe=False)


class AddGameCreateAPIView(CreateAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class GamesListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

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
