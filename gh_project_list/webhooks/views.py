from webhooks.serializers import WebhookSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsOwnerOrReadOnly
from webhooks.models import Webhook


class WebhookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing webhook instances.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    serializer_class = WebhookSerializer
    queryset = Webhook.objects.all()
