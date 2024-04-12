from rest_framework import serializers
from tutorias.models import *

#serializer para listar, crear y detallar tutores
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'

class TutoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoria
        fields = '__all__'