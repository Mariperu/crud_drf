from rest_framework import routers
from .api import ProjectViewSet

#creando crud
router = routers.DefaultRouter()

# (nombre de ruta, view set qeu viene de api.py, nombre de ruta )
router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls