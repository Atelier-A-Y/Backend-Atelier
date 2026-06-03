from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Roupa
from uploader.models import Image
from uploader.serializers import ImageSerializer


class RoupaRetrieveSerializer(ModelSerializer):
    foto = ImageSerializer(required=False)

    class Meta:
        model = Roupa
        fields = '__all__'
        depth = 1

class RoupaSerializer(ModelSerializer):
    class Meta:
        model = Roupa
        fields = '__all__'

class RoupaCreateSerializer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(
        source='foto',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Roupa
        fields = '__all__'
