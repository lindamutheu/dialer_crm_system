from django.contrib import admin
from .models import Integration, Tag, IntegrationLog, IntegrationCredential, WebhookEvent


@admin.register(IntegrationCredential)
class IntegrationCredentialAdmin(admin.ModelAdmin):
 list_display = ('name', 'provider', 'is_active', 'created_at')
search_fields = ('name', 'provider')


@admin.register(IntegrationLog)
class IntegrationLogAdmin(admin.ModelAdmin):
 list_display = ('provider', 'action', 'status', 'created_at')
readonly_fields = ('request_data', 'response_data')
search_fields = ('provider', 'action')


@admin.register(WebhookEvent)
class WebhookEventAdmin(admin.ModelAdmin):
 list_display = ('event_type', 'received_at')
readonly_fields = ('payload',)


@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active', 'created_at')
    search_fields = ('name', 'description')



