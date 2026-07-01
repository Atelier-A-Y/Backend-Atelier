from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Favorito


class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['nota', 'comentario']

    def create(self, validated_data):
        # Pega usuario e roupa do contexto
        usuario = self.context['usuario']
        roupa = self.context['roupa']

        # Adiciona usuario e roupa aos dados validados
        validated_data['usuario'] = usuario
        validated_data['roupa'] = roupa

        return super().create(validated_data)


class FavoritoDetailSerializer(ModelSerializer):
    roupa_nome = SerializerMethodField()

    class Meta:
        model = Favorito
        fields = '__all__'

    def get_roupa_nome(self, obj):
        return obj.roupa.nome
