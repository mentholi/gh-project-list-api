from rest_framework import serializers
from webhooks.models import Webhook


class WebhookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    url = serializers.URLField()

    class Meta:
        model = Webhook
        fields = [
            'id',
            'user',
            'url',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'user',
            'created_at',
            'updated_at',
        ]
