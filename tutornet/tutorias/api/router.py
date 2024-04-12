from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tutorias.api.views import TutorViewSet, EstudianteViewSet, AgendaViewSet, TutoriaViewSet

router = DefaultRouter()
router.register(r'tutores', TutorViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'tutorias', TutoriaViewSet)
router.register(r'agendas', AgendaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]