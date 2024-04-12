from rest_framework import viewsets
from tutorias.models import Agenda, Tutor, Estudiante, Tutoria
from tutorias.api.serializers import TutorSerializer, EstudianteSerializer, TutoriaSerializer, AgendaSerializer

class TutorViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Tutor."""
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Estudiante."""
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class TutoriaViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Tutoria."""
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Agenda."""
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer