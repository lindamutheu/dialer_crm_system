from rest_framework import serializers
from .models import Integration, Tag, IntegrationLog, IntegrationCredential, WebhookEvent

class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = '__all__'


class IntegrationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationLog
        fields = '__all__'

class IntegrationCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationCredential
        fields = '__all__'

class WebhookEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookEvent
        fields = '__all__'

