from rest_framework import serializers
from .models import (
    Message, MessageReaction, MessageReadReceipt, UserPresence,
    Conversation, ConversationMember, Attachment,
    ScheduledMessage, AutoResponder, MessageQueue,
    MessageTemplateUsage, MessageForwarding
)
from Accounts.models import userProfile
from Templates.models import Template  # Update this import if needed

class MessageSerializer(serializers.ModelSerializer):
    reactions = serializers.SerializerMethodField()
    read_receipts = serializers.SerializerMethodField()
    attachments = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            "id", "sender", "recipient", "content", "timestamp",
            "reactions", "read_receipts", "attachments"
        ]
        read_only_fields = ["timestamp"]

    def get_reactions(self, obj):
        return MessageReactionSerializer(obj.reactions.all(), many=True).data

    def get_read_receipts(self, obj):
        return MessageReadReceiptSerializer(obj.read_receipts.all(), many=True).data

    def get_attachments(self, obj):
        return AttachmentSerializer(obj.attachments.all(), many=True).data


class MessageReactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = MessageReaction
        fields = ["id", "user", "emoji", "reacted_at"]
        read_only_fields = ["reacted_at"]

class MessageReadReceiptSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = MessageReadReceipt
        fields = ["id", "user", "read_at"]
        read_only_fields = ["read_at"]

class UserPresenceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserPresence
        fields = ["id", "user", "is_online", "last_seen"]
        read_only_fields = ["last_seen"]


    class ConversationSerializer(serializers.ModelSerializer):

     class Meta:
        model = Conversation
        fields = [
            "id", "name", "conversation_type",
            "created_by", "created_at", "members"
        ]

    def get_members(self, obj):
        return ConversationMemberSerializer(obj.members.all(), many=True).data


class ConversationMemberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = ConversationMember
        fields = ["id", "user", "joined_at"]
        read_only_fields = ["joined_at"]

class MessageForwardingSerializer(serializers.ModelSerializer):
    original_message = MessageSerializer()
    forwarded_to = serializers.StringRelatedField()

    class Meta:
        model = MessageForwarding
        fields = ["id", "original_message", "forwarded_to", "forwarded_at"]
        read_only_fields = ["forwarded_at"]

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ["id", "file", "uploaded_at"]
        read_only_fields = ["uploaded_at"]


class ScheduledMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledMessage
        fields = ["id", "message", "scheduled_time", "is_sent"]
        read_only_fields = ["is_sent"]

class AutoResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoResponder
        fields = ["id", "trigger_keyword", "response_message", "is_active"]
        read_only_fields = ["is_active"]

class MessageQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageQueue
        fields = ["id", "message", "queued_at", "processed"]
        read_only_fields = ["queued_at", "processed"]

        