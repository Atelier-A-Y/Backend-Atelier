from rest_framework.serializers import (
    DecimalField,
    IntegerField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    SlugRelatedField,
    ValidationError,
)

from core.models import Roupa
from uploader.models import Image
from uploader.serializers import ImageSerializer


class RoupaAdicionarAoCarrinhoSerializer(Serializer):
    quantidade = IntegerField(default=1, min_value=1)

    def validate(self, data):
        roupa = self.context.get('roupa')
        if not roupa:
            raise ValidationError('Roupa não fornecida no contexto.')
        if data['quantidade'] > roupa.quantidade:
            raise ValidationError('Quantidade solicitada não disponível em estoque.')
        return data


class RoupaAjustarEstoqueSerializer(Serializer):
    quantidade = IntegerField()

    def validate_quantidade(self, value):
        roupa = self.context.get('roupa')
        if roupa:
            nova_quantidade = roupa.quantidade + value
            if nova_quantidade < 0:
                raise ValidationError('A quantidade em estoque não pode ser negativa.')
        return value


class RoupaAlterarPrecoSerializer(Serializer):
    preco = DecimalField(max_digits=10, decimal_places=2)

    def validate_preco(self, value):
        """Valida se o preço é um valor positivo."""
        if value <= 0:
            raise ValidationError('O preço deve ser um valor positivo.')
        return value


class RoupaComFavoritosSerializer(ModelSerializer):
    media_notas = SerializerMethodField()
    total_favoritos = SerializerMethodField()
    comentarios = SerializerMethodField()

    class Meta:
        model = Roupa
        fields = ['id', 'nome', 'media_notas', 'total_favoritos', 'comentarios']

    def get_media_notas(self, obj):
        notas = obj.favoritos.exclude(nota__isnull=True).values_list('nota', flat=True)
        if not notas:
            return 0
        return sum(notas) / len(notas)

    def get_total_favoritos(self, obj):
        return obj.favoritos.count()

    def get_comentarios(self, obj):
        return obj.favoritos.exclude(comentario__isnull=True).values('usuario__email', 'comentario', 'nota')


class RoupaListSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Roupa
        fields = ['id', 'nome', 'preco', 'quantidade', 'categoria', 'capa']
        depth = 1


class RoupaRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Roupa
        fields = '__all__'
        depth = 1


class RoupaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Roupa
        fields = '__all__'