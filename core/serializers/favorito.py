from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from core.serializers.roupa import RoupaRetrieveSerializer
from core.models import Favorito, Roupa


class FavoritoSerializer(ModelSerializer):
    roupa = PrimaryKeyRelatedField(
        queryset=Roupa.objects.all()
    )

    class Meta:
        model = Favorito
        fields = "__all__"
        read_only_fields = ["usuario"]


class FavoritoRetrieveSerializer(ModelSerializer):
    roupa = RoupaRetrieveSerializer(read_only=True)

    class Meta:
        model = Favorito
        fields = "__all__"
