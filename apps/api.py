from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all()# all: consulta todo los datos
  #Permisos para manejar data: AllowAny or auth
  permission_classes = [permissions.AllowAny]
  serializer_class = ProjectSerializer