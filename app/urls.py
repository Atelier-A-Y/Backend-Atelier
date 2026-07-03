from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from core.views import (
    CarrinhoViewSet,
    CategoriaViewSet,
    CompraFornecedorViewSet,
    CompraViewSet,
    ContinenteViewSet,
    FornecedorViewSet,
    EstoqueViewSet,
    FavoritoViewSet,
    RoupaViewSet,
    TamanhoViewSet,
    TipoPagamentoViewSet,
    UserRegistrationView,
    UserViewSet,
    VendaViewSet,
)

router = DefaultRouter()

router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'compras', CompraViewSet, basename='compras')
router.register(r'continentes', ContinenteViewSet, basename='continentes')
router.register(r'roupas', RoupaViewSet, basename='roupas')
router.register(r'tamanhos', TamanhoViewSet, basename='tamanhos')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'tipoPagamento', TipoPagamentoViewSet, basename='tipoPagamento')
router.register(r'vendas', VendaViewSet, basename='vendas')
router.register(r'fornecedores', FornecedorViewSet, basename='fornecedores')
router.register(r'comprasFornecedores', CompraFornecedorViewSet, basename='comprasFornecedores')
router.register(r'estoque', EstoqueViewSet, basename='estoque')
router.register(r'carinhos', CarrinhoViewSet, basename='carinhos')
router.register(r'favoritos', FavoritoViewSet, basename='favoritos')


urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/doc/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # Autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Registro de usuários
    path('api/registro/', UserRegistrationView.as_view(), name='user_registration'),
    # API
    path('api/', include(router.urls)),
]
