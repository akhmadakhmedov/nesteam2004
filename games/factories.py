import factory
from .models import Genre, Game

class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre
    name = factory.Sequence(lambda n:f'Test Genre {n}')

class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game
    name = factory.Sequence(lambda n:f'Test Game {n}')