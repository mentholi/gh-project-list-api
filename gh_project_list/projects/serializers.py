from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    link = serializers.URLField()

    class Meta:
        model = Project
        fields = [
            'id',
            'user',
            'name',
            'description',
            'created_at',
            'updated_at',
            'link',
            'rating',
        ]
        read_only_fields = [
            'user',
            'created_at',
            'updated_at',
        ]
