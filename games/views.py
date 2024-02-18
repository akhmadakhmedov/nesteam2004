from django.http import JsonResponse
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .paginations import *
from .filters import GameFilter
from rest_framework import filters


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
    pagination_class = GamePagination
    serializer_class = GameSerializer
    queryset = Game.objects.all()




class GamesSearchView(APIView):
    def get(self, request):
        if 'key_word' in request.GET:
            key_word = request.GET['key_word']
        elif 'key_word' in request.data:
            key_word = request.data['key_word']
        else:
            return Response('no data', status=400)
        games = Game.objects.filter(
            Q(name__icontains = key_word) |
            Q(genre__name__icontains = key_word) |
            Q(studio__name__icontains = key_word)
        )
        serializer = GameSerializer(instance=games, many=True)
        json_data = serializer.data
        return Response(data=json_data)

#def studio(request):
#    studio_list = Studio.objects.all()
#    serializer = StudioSerializer(studio_list, many=True)
#    data = serializer.data
#    return JsonResponse(data, safe=False)

class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    #permission_classes = [IsAuthenticated]



class StudiosCreateAPIView(CreateAPIView):
    serializer_class = StudioSerializer
    queryset = Studio.objects.all()

class GenreViewSet(ModelViewSet):
    pagination_class = GenrePagination
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class GameCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializers = GameSerializer(data=data)
        if serializers.is_valid():
            game = Game()
            game.name = serializers.validated_data["name"]
            game.year = serializers.validated_data["year"]
            game.genre = serializers.validated_data["genre"]
            game.studio = serializers.validated_data["studio"]
            game.save()
            serializers = GameSerializer(instance=game)
            return Response(data=serializers.data, status=201)
        else:
            errors = serializers.error_messages
            response_data = {
                "message": "Not valid data",
                "errors": errors
            }
            return Response(response_data, status=400)

class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()