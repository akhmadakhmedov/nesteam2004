from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *
from .factories import GenreFactory, GameFactory

class GameCreateAPITestCase(APITestCase):
    def test_create_game_should_success(self):
        Genre(
            name = "test genre 1",
            description = "test description 1"
        ).save()
        Studio(
            name = "test studio 1",
            workers_count = 15,
            games_count = 24
        ).save()
        data = {
            "name": "New Game One",
            "year": 2000,
            "genre": 1,
            "studio": 1
        }
        response = self.client.post(
            '/game-create/', data
        )
        self.assertEqual(response.status_code, 201)
        game = Game.objects.last()
        self.assertEqual(game.name, data['name'])
        self.assertEqual(game.year, data['year'])
        self.assertEqual(game.genre.id, data['genre'])
        self.assertEqual(game.studio.id, data['studio'])

    def test_create_game_with_wrong_info_should_fail(self):
        response = self.client.post('/game-create/', {"test 1": "lorem"})
        self.assertEqual(response.status_code, 400)

    def test_create_game_via_get_request_should_response_405(self):
        data = {
            "name": "wrong form",
            "year": 2000,
            "genre": 1,
            "studio": 1
        }
        response = self.client.get('/game-create/', data)
        self.assertEqual(response.status_code, 405)
        games_exists = Game.objects.filter(name="Wrong form").exists()
        self.assertFalse(games_exists)

class GenreListTest(APITestCase):
    def setUp(self):
        self.genre_1 = GenreFactory()
        self.genre_2 = GenreFactory()
        self.genre_3 = GenreFactory()

    def test_get_list_of_3_genres(self):
        response = self.client.get('/genre/genre-api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.genre_1.name, response.data[0]['name'])

    def test_get_genre_detail(self):
        response = self.client.get(f'/genre/genre-api/{self.genre_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.genre_1.name, response.data['name'])

class GameListTest(APITestCase):
    def test_get_list_of_3_games(self):
        game_1 = GameFactory()
        game_2 = GameFactory()
        game_3 = GameFactory()
        response = self.client.get('/game/game-api/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(game_1.name, response.data[0]['name'])

    def test_get_game_detail(self):
        game_1 = GameFactory()
        response = self.client.get(f'/game/game-api/{game_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(game_1.name, response.data['name'])




