from rest_framework.serializers import ModelSerializer
from core.serializers import RoupaRetrieveSerializer
from core.models import Favorito


class FavoritoSerializer(ModelSerializer):
    roupa = RoupaRetrieveSerializer(read_only=True)
    class Meta:
        model = Favorito
        fields = '__all__'
