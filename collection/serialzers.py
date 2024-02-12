from rest_framework.serializers import ModelSerializer
from .models import GameCollection

class GameCollectionSerializer(ModelSerializer):
    class Meta:
        model = GameCollection
        fields = "__all__"