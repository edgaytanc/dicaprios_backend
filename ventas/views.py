from rest_framework import viewsets
from .models import Pedido
from .models import DetallePedido
from .models import Factura
from .models import DetalleFactrua
from .serializers import PedidoSerializer
from .serializers import DetallePedidoSerializer
from .serializers import FacturaSerializer
from .serializers import DetalleFacturaSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactrua.objects.all()
    serializer_class = DetalleFacturaSerializer
