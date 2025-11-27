from django.db import models
from Accounts.models import userProfile

class Call(models.Model):
    CALL_TYPE_CHOICES = (
        ('outbound', 'Outbound'),
        ('inbound', 'Inbound'),
    )

    CALL_STATUS_CHOICES = (
        ('initiated', 'Initiated'),
        ('ringing', 'Ringing'),
        ('answered', 'Answered'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('busy', 'Busy'),
        ('no_answer', 'No Answer'),
    )

    call_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(userProfile, on_delete=models.SET_NULL, null=True, related_name="agent_calls")
    phone_number = models.CharField(max_length=20)
    call_type = models.CharField(max_length=10, choices=CALL_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=CALL_STATUS_CHOICES, default='initiated')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration_seconds = models.IntegerField(null=True, blank=True)
    recording_url = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} ({self.status})"

class CallQueue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    agents = models.ManyToManyField(userProfile, related_name="call_queues")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CallSchedule(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE, related_name="schedules")
    scheduled_time = models.DateTimeField()
    is_executed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Call {self.call.call_id} scheduled at {self.scheduled_time}"
    

class CallDisposition(models.Model):
    call = models.ForeignKey(Call, on_delete=models.CASCADE, related_name="dispositions")
    disposition_code = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Disposition for Call {self.call.call_id}: {self.disposition_code}"
    
    class CallStatistic(models.Model):
        agent = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name="call_statistics")
        total_calls = models.IntegerField(default=0)
        answered_calls = models.IntegerField(default=0)
        average_call_duration = models.FloatField(default=0.0)  # in seconds

        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"Statistics for Agent {self.agent.user.username}"
        

class CallCampaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class CampaignCall(models.Model):
        campaign = models.ForeignKey(CallCampaign, on_delete=models.CASCADE, related_name="campaign_calls")
        call = models.ForeignKey(Call, on_delete=models.CASCADE, related_name="in_campaigns")

        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"Call {self.call.call_id} in Campaign {self.campaign.name}"
        
        class AgentStatus(models.Model):
            agent = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name="status_records")
            status = models.CharField(max_length=50)
            last_updated = models.DateTimeField(auto_now=True)

            def __str__(self):
                return f"Status of Agent {self.agent.user.username}: {self.status}"
            
            class CallRecording(models.Model):
                call = models.ForeignKey(Call, on_delete=models.CASCADE, related_name="recordings")
                recording_url = models.URLField()
                duration_seconds = models.IntegerField()

                created_at = models.DateTimeField(auto_now_add=True)

                def __str__(self):
                    return f"Recording for Call {self.call.call_id}"