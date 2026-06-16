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
    CategoriaViewSet,
    CompraViewSet,
    ContinenteViewSet,
    RoupaViewSet,
    TamanhoViewSet,
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
router.register(r'vendas', VendaViewSet, basename='vendas')

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
