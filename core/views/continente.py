from rest_framework.viewsets import ModelViewSet

from core.models import Continente
from core.serializers import ContinenteSerializer


class ContinenteViewSet(ModelViewSet):
    queryset = Continente.objects.all()
    serializer_class = ContinenteSerializer
