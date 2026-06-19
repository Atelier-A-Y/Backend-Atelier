from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'telefone', 'cpf']
        depth = 1


class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'telefone', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
