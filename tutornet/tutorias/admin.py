from django.contrib import admin

from tutorias.models import Agenda, Estudiante, Tutor, Tutoria
# Register your models here.
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        "tutoria",
        "estudiante",
    )

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "last_name",
        "created_at",
    )

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "last_name",
        "created_at",
    )

@admin.register(Tutoria)
class TutoriaAdmin(admin.ModelAdmin):
    list_display = (
        "materia",
        "date",
        "time",
        "tutor",
    )