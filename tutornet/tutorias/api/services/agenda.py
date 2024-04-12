from rest_framework import viewsets
from tutorias.models import Agenda
from tutorias.api.serializers import AgendaSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Agenda."""
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer