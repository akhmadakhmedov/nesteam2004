from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *

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


