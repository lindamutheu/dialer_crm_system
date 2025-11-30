from django.db import models

class Integration(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    endpoint_url = models.URLField(max_length=500)
    integration_type = models.CharField(max_length=100)
    last_synced = models.DateTimeField(blank=True, null=True)
    config = models.JSONField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    schedule = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
   
class IntegrationCredential(models.Model):

  PROVIDER_CHOICES = (
('twilio', 'Twilio'),
('sendgrid', 'SendGrid'),
('whatsapp', 'WhatsApp'),
('sms_gateway', 'Generic SMS Gateway'),
('payments', 'Payments'),
)


name = models.CharField(max_length=100)
provider = models.CharField(max_length=50, choices=PROVIDER_CHOICES)
api_key = models.CharField(max_length=512, blank=True, null=True)
api_secret = models.CharField(max_length=512, blank=True, null=True)
config = models.JSONField(blank=True, null=True)
is_active = models.BooleanField(default=True)
created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.name} ({self.provider})"


class IntegrationLog(models.Model):

 provider = models.CharField(max_length=100)
action = models.CharField(max_length=100)
request_data = models.JSONField(blank=True, null=True)
response_data = models.JSONField(blank=True, null=True)
status = models.CharField(max_length=50, blank=True, null=True)
created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.provider} {self.action} @ {self.created_at}"




class WebhookEvent(models.Model):
        integration = models.ForeignKey(Integration, on_delete=models.CASCADE)
        event_type = models.CharField(max_length=100)
        payload = models.JSONField()
        received_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.integration.name} - {self.event_type} at {self.received_at}"
        
