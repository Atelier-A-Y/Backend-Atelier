from rest_framework.serializers import ModelSerializer

from core.models import Roupa


class RoupaSerializer(ModelSerializer):
    class Meta:
        model = Roupa
        fields = '__all__'
