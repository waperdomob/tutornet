from rest_framework import viewsets
from tutorias.models import Estudiante
from tutorias.api.serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Estudiante."""
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer