from rest_framework import viewsets
from tutorias.models import Tutoria
from tutorias.api.serializers import TutoriaSerializer

class TutoriaViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Tutoria."""
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer