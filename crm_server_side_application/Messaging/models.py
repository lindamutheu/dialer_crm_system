from django.db import models


class Message(models.Model):
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.recipient} at {self.timestamp}"


class MessageReaction(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=10)  # emoji string
    reacted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('message', 'user', 'emoji')

    def __str__(self):
        return f"{self.user.username} reacted {self.emoji}"


class MessageReadReceipt(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='read_receipts')
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('message', 'user')

    def __str__(self):
        return f"{self.user.username} read message {self.message.id}"

class UserPresence(models.Model):
    user = models.OneToOneField(userProfile, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {'Online' if self.is_online else 'Offline'}"


class Conversation(models.Model):
    CONVERSATION_TYPES = (
        ('direct', 'Direct'),
        ('group', 'Group'),
    )

    name = models.CharField(max_length=255, blank=True, null=True)
    conversation_type = models.CharField(max_length=20, choices=CONVERSATION_TYPES)
    created_by = models.ForeignKey(userProfile, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.conversation_type == 'direct':
            return f"Direct Chat {self.id}"
        return self.name or f"Group Chat {self.id}"


class ConversationMember(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE, related_name='conversations')
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = ('conversation', 'user')

    def __str__(self):
        return f"{self.user.username} in {self.conversation}"



class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for message ID {self.message.id} uploaded at {self.uploaded_at}"


class ScheduledMessage(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='scheduled_messages')
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scheduled message ID {self.message.id} for {self.scheduled_time}"
    

class AutoResponder(models.Model):
    trigger_phrase = models.CharField(max_length=255)
    response_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='auto_responses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AutoResponder for phrase '{self.trigger_phrase}' created at {self.created_at}"

class MessageQueue(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='queue_entries')
    queued_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Message ID {self.message.id} queued at {self.queued_at}, processed: {self.processed}"
    
class MessageTemplateUsage(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='usages')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='template_usages')
    used_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Template '{self.template.name}' used in message ID {self.message.id} at {self.used_at}"
    
class MessageForwarding(models.Model):
    original_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='forwards')
    forwarded_to = models.CharField(max_length=255)
    forwarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message ID {self.original_message.id} forwarded to {self.forwarded_to} at {self.forwarded_at}"


    