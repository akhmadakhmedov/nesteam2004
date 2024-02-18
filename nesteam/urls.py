"""
URL configuration for nesteam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from games.views import *
from rest_framework import routers
from .yasg import urlpatterns as doc_urls
#from game_collection.views import *


router_genre = routers.DefaultRouter()
router_studio = routers.DefaultRouter()
router_game = routers.DefaultRouter()
router_genre.register(r'genre-api', GenreViewSet)
router_studio.register(r'studio-api', StudioViewSet)
router_game.register(r'game-api', GameViewSet)
#router.register(r'game-collecton', GameCollectionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('games/', GamesListAPIView.as_view(), name='games'),
    #path('create-game/', CreateGameAPIView.as_view(), name='create-game'),
    path('game-create/', GameCreateAPIView.as_view(), name='game-create'),
    path('games-view/', GamesView.as_view(), name='games-view'),
    path('games-search/', GamesSearchView.as_view(), name='games-search'),
    path('studios/', StudiosListAPIView.as_view(), name='studios'),
    path('create-studio/', StudiosCreateAPIView.as_view(), name='create-studio'),
    path('users/', include("usersapp.urls")),
    path('collections/', include("collection.urls")),
    path('genre/', include(router_genre.urls)),
    path('studio/', include(router_studio.urls)),
    path('game/', include(router_game.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
urlpatterns += doc_urls
