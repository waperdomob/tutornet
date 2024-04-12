from rest_framework import viewsets
from tutorias.models import Tutor
from tutorias.api.serializers import TutorSerializer

class TutorViewSet(viewsets.ModelViewSet):
    """Conjunto de vistas para el modelo Tutor."""
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
