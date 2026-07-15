from rest_framework.serializers import ModelSerializer

from core.models import Compra


class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ("user",)
