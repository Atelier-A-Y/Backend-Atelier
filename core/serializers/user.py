from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import User


class UserSerializer(ModelSerializer):
    foto_perfil = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'telefone', 'cpf', 'foto_perfil']
        depth = 1

    def get_foto_perfil(self, obj):
        if obj.foto_perfil:
            return obj.foto_perfil.url
        return None


class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'telefone', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
