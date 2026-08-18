from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from core.models import Favorito, Roupa
from .roupa_serializers import RoupaRetrieveSerializer


class FavoritoSerializer(ModelSerializer):

    roupa = RoupaRetrieveSerializer(read_only=True)

    roupa_id = PrimaryKeyRelatedField(
        source='roupa',
        queryset=Roupa.objects.all(),
        write_only=True
    )

    class Meta:
        model = Favorito
        fields = [
            'id',
            'roupa',
            'roupa_id',
            'usuario',
            'data_criacao',
            'data_atualizacao',
        ]
        read_only_fields = ['usuario']