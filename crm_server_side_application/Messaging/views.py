from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import (
    Message, MessageReaction, MessageReadReceipt, UserPresence,
    Conversation, ConversationMember, Attachment, ScheduledMessage,
    AutoResponder, MessageQueue, MessageTemplateUsage, MessageForwarding
)
from .serializers import (
    MessageSerializer, MessageReactionSerializer, MessageReadReceiptSerializer,
    UserPresenceSerializer, ConversationSerializer, ConversationMemberSerializer,
    AttachmentSerializer, ScheduledMessageSerializer, AutoResponderSerializer,
    MessageQueueSerializer, MessageTemplateUsageSerializer, MessageForwardingSerializer
)


# MESSAGE VIEWSET 

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-timestamp')
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]


# REACTION VIEWSET 

class MessageReactionViewSet(viewsets.ModelViewSet):
    queryset = MessageReaction.objects.all()
    serializer_class = MessageReactionSerializer
    permission_classes = [permissions.AllowAny]


#READ RECEIPT VIEWSET 

class MessageReadReceiptViewSet(viewsets.ModelViewSet):
    queryset = MessageReadReceipt.objects.all()
    serializer_class = MessageReadReceiptSerializer
    permission_classes = [permissions.AllowAny]


# USER PRESENCE VIEWSET

class UserPresenceViewSet(viewsets.ModelViewSet):
    queryset = UserPresence.objects.all()
    serializer_class = UserPresenceSerializer
    permission_classes = [permissions.AllowAny]


# VIEWSET

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer
    permission_classes = [permissions.AllowAny]


# CONVERSATION MEMBERS VIEWSET

class ConversationMemberViewSet(viewsets.ModelViewSet):
    queryset = ConversationMember.objects.all()
    serializer_class = ConversationMemberSerializer
    permission_classes = [permissions.AllowAny]


#ATTACHMENT VIEWSET

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.AllowAny]


#SCHEDULED MESSAGE VIEWSET

class ScheduledMessageViewSet(viewsets.ModelViewSet):
    queryset = ScheduledMessage.objects.all()
    serializer_class = ScheduledMessageSerializer
    permission_classes = [permissions.AllowAny]


#AUTO RESPONDER VIEWSET

class AutoResponderViewSet(viewsets.ModelViewSet):
    queryset = AutoResponder.objects.all()
    serializer_class = AutoResponderSerializer
    permission_classes = [permissions.AllowAny]


#MESSAGE QUEUE VIEWSET

class MessageQueueViewSet(viewsets.ModelViewSet):
    queryset = MessageQueue.objects.all()
    serializer_class = MessageQueueSerializer
    permission_classes = [permissions.AllowAny]


#TEMPLATE USAGE VIEWSET

class MessageTemplateUsageViewSet(viewsets.ModelViewSet):
    queryset = MessageTemplateUsage.objects.all()
    serializer_class = MessageTemplateUsageSerializer
    permission_classes = [permissions.AllowAny]


#MESSAGE FORWARDING VIEWSET

class MessageForwardingViewSet(viewsets.ModelViewSet):
    queryset = MessageForwarding.objects.all()
    serializer_class = MessageForwardingSerializer
    permission_classes = [permissions.AllowAny]
