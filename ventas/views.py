from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pedido
from .models import DetallePedido
from .models import Factura
from .models import DetalleFactrua
from .serializers import PedidoSerializer
from .serializers import DetallePedidoSerializer
from .serializers import FacturaSerializer
from .serializers import DetalleFacturaSerializer
from .filters import DetallePedidoFilter

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cliente', 'fecha', 'estado']
    

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DetallePedidoFilter

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactrua.objects.all()
    serializer_class = DetalleFacturaSerializer
