from django.shortcuts import get_object_or_404
from projects.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsOwnerOrReadOnly
from projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
