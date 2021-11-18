from django.shortcuts import get_object_or_404
from projects.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsOwnerOrReadOnly
from projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at', 'updated_at']
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
