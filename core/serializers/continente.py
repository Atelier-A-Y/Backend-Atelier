from rest_framework.serializers import ModelSerializer

from core.models import Continente


class ContinenteSerializer(ModelSerializer):
    class Meta:
        model = Continente
        fields = '__all__'
