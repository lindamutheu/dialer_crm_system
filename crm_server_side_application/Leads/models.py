from django.db import models
from Accounts.models import userProfile
from Accounts import models as account_models
from Dialer import models as dialer_models

class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class LeadStatus(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lead} - {self.status}"
    
class LeadSource(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='sources')
    source = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead} - {self.source}"
    
class LeadNote(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.lead} at {self.created_at}"
    
class LeadActivity(models.Model):
    ACTIVITY_CHOICES = (
        ('call', 'Call'),
        ('email', 'Email'),
        ('meeting', 'Meeting'),
        ('note', 'Note'),
    )

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='activities')
    agent = models.ForeignKey(userProfile, on_delete=models.SET_NULL, null=True)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    notes = models.TextField(blank=True, null=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.activity_type} for {self.lead}"


class LeadAssignment(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='assignments')
    agent = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name='lead_assignments')
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead} assigned to {self.agent}"
    


    
class LeadTag(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tag} for {self.lead}"
    
class LeadCampaign(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='campaigns')
    campaign_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.campaign_name} for {self.lead}"
    
class LeadConversion(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='conversions')
    converted_at = models.DateTimeField(auto_now_add=True)
    converted_by = models.ForeignKey(userProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.lead} converted at {self.converted_at}"
    
class LeadFollowUp(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='follow_ups')
    follow_up_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Follow-up for {self.lead} on {self.follow_up_date}"
    

class LeadDocument(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(upload_to='lead_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.lead} uploaded at {self.uploaded_at}"
    
class LeadPriority(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='priorities')
    priority_level = models.CharField(max_length=50)
    set_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead} - {self.priority_level}"
    

class LeadReminder(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='reminders')
    reminder_date = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.lead} on {self.reminder_date}"
    

class LeadScore(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name='score')
    score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lead} score: {self.score}"

# Integration with Dialer System

class LeadCall(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="calls")
    call = models.ForeignKey(Call, on_delete=models.CASCADE, related_name="lead_calls")
    campaign = models.ForeignKey(CallCampaign, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Call {self.call.call_id} for Lead {self.lead}"