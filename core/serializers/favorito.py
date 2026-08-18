from core.models.roupa import Roupa
from rest_framework.serializers import ModelSerializer
from core.serializers import RoupaSerializer
from core.models import Favorito


class FavoritoSerializer(ModelSerializer):
    roupa = RoupaSerializer(read_only=True)
    class Meta:
        model = Favorito
        fields = '__all__'
