from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Favorito, Roupa
from core.serializers.favorito import (
    FavoritoDetailSerializer,
    FavoritoSerializer,
)
from core.serializers.roupa import RoupaComFavoritosSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Listar favoritos",
        description="Retorna a lista de roupas favoritadas pelo usuário autenticado.",
        responses={200: FavoritoDetailSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Detalhar favorito",
        description="Retorna os dados de um favorito específico do usuário autenticado.",
        responses={200: FavoritoSerializer},
    ),
    create=extend_schema(
        summary="Adicionar favorito",
        description="Adiciona uma roupa à lista de favoritos do usuário autenticado.",
        request=FavoritoSerializer,
        responses={201: FavoritoSerializer, 400: None},
    ),
    update=extend_schema(
        summary="Atualizar favorito",
        description="Atualiza os dados (nota e/ou comentário) de um favorito específico.",
        request=FavoritoSerializer,
        responses={200: FavoritoSerializer, 400: None, 404: None},
    ),
    partial_update=extend_schema(
        summary="Atualizar favorito parcialmente",
        description="Atualiza parcialmente os dados de um favorito específico.",
        request=FavoritoSerializer,
        responses={200: FavoritoSerializer, 400: None, 404: None},
    ),
    destroy=extend_schema(
        summary="Remover favorito",
        description="Remove uma roupa da lista de favoritos do usuário autenticado.",
        responses={204: None, 404: None},
    ),
)
class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

    def get_queryset(self):
        # Filtra favoritos apenas do usuário logado
        return self.queryset.filter(usuario=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoritoDetailSerializer
        return FavoritoSerializer

    def perform_create(self, serializer):
        # Automaticamente define o usuário como o usuário logado
        serializer.save(usuario=self.request.user)

    @extend_schema(
        summary="Roupas com estatísticas de favoritos",
        description="Retorna as roupas que possuem ao menos um favorito, com média de notas, total de favoritos e lista de comentários.",
        responses={200: RoupaComFavoritosSerializer(many=True)},
    )
    @action(detail=False, methods=['get'])
    def roupas_com_estatisticas(self, request):
        # Retorna apenas as roupas que têm favoritos
        roupas = Roupa.objects.filter(favoritos__isnull=False).distinct()
        serializer = RoupaComFavoritosSerializer(roupas, many=True)
        return Response(serializer.data)
