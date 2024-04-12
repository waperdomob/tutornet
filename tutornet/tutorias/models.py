from django.db import models

# Create your models here.
class Tutor(models.Model):
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

class Estudiante(models.Model):
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)

class Tutoria(models.Model):
    materia = models.CharField(max_length=45)    
    date = models.DateField()
    time = models.TimeField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.materia)

class Agenda(models.Model):
    tutoria = models.ForeignKey(Tutoria, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.tutoria.materia)