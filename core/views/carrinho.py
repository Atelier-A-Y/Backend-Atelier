from rest_framework.viewsets import ModelViewSet

from core.models import Carinho
from core.serializers import CarinhoSerializer


class CarinhoViewSet(ModelViewSet):
    queryset = Carinho.objects.all()
    serializer_class = CarinhoSerializer
