from rest_framework import serializers
from .models import (
    Lead, LeadStatus, LeadSource, LeadNote, LeadActivity,
    LeadAssignment, LeadTag, LeadCampaign, LeadConversion,
    LeadFollowUp, LeadDocument, LeadPriority, LeadReminder,
    LeadScore, LeadCall
)
from Accounts.models import userProfile
from Dialer.serializers import CallSerializer, CallCampaignSerializer

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    statuses = serializers.StringRelatedField(many=True)
    sources = serializers.StringRelatedField(many=True)
    notes = serializers.StringRelatedField(many=True)
    activities = serializers.StringRelatedField(many=True)
    assignments = serializers.StringRelatedField(many=True)
    tags = serializers.StringRelatedField(many=True)
    campaigns = serializers.StringRelatedField(many=True)
    conversions = serializers.StringRelatedField(many=True)
    follow_ups = serializers.StringRelatedField(many=True)
    documents = serializers.StringRelatedField(many=True)
    priorities = serializers.StringRelatedField(many=True)
    reminders = serializers.StringRelatedField(many=True)
    score = serializers.StringRelatedField()

    class Meta:
        model = Lead
        fields = "__all__"


class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"


# Lead Status
class LeadStatusSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadStatus
        fields = "__all__"


class LeadStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadStatus
        fields = "__all__"


# Lead Source
class LeadSourceSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadSource
        fields = "__all__"


class LeadSourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadSource
        fields = "__all__"


# Lead Note
class LeadNoteSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadNote
        fields = "__all__"


class LeadNoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadNote
        fields = "__all__"


# Lead Activity
class LeadActivitySerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    agent = serializers.StringRelatedField()

    class Meta:
        model = LeadActivity
        fields = "__all__"


class LeadActivityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadActivity
        fields = "__all__"


# Lead Assignment
class LeadAssignmentSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    agent = serializers.StringRelatedField()

    class Meta:
        model = LeadAssignment
        fields = "__all__"


class LeadAssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadAssignment
        fields = "__all__"


# Lead Tag
class LeadTagSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadTag
        fields = "__all__"


class LeadTagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadTag
        fields = "__all__"


# Lead Campaign
class LeadCampaignSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadCampaign
        fields = "__all__"


class LeadCampaignCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadCampaign
        fields = "__all__"


# Lead Conversion
class LeadConversionSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    converted_by = serializers.StringRelatedField()

    class Meta:
        model = LeadConversion
        fields = "__all__"


class LeadConversionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadConversion
        fields = "__all__"


# Lead Follow-up
class LeadFollowUpSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadFollowUp
        fields = "__all__"


class LeadFollowUpCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadFollowUp
        fields = "__all__"


# Lead Document
class LeadDocumentSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadDocument
        fields = "__all__"


class LeadDocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadDocument
        fields = "__all__"


# Lead Priority
class LeadPrioritySerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadPriority
        fields = "__all__"


class LeadPriorityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadPriority
        fields = "__all__"


# Lead Reminder
class LeadReminderSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadReminder
        fields = "__all__"


class LeadReminderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadReminder
        fields = "__all__"


# Lead Score
class LeadScoreSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)

    class Meta:
        model = LeadScore
        fields = "__all__"


class LeadScoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadScore
        fields = "__all__"


# Lead Call (Integration with Dialer)
class LeadCallSerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    call = CallSerializer(read_only=True)
    campaign = CallCampaignSerializer(read_only=True)

    class Meta:
        model = LeadCall
        fields = "__all__"


class LeadCallCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadCall
        fields = "__all__"
