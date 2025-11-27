from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Lead, LeadStatus, LeadSource, LeadNote, LeadActivity
from .serializers import (
    LeadSerializer,
    LeadStatusSerializer,
    LeadStatusCreateSerializer,
    LeadSourceSerializer,
    LeadSourceCreateSerializer,
    LeadNoteSerializer,
    LeadNoteCreateSerializer,
    LeadActivitySerializer,
    LeadActivityCreateSerializer,
)



# Lead ViewSet

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadCreateSerializer
        return LeadSerializer


# LeadStatus ViewSet

class LeadStatusViewSet(viewsets.ModelViewSet):
    queryset = LeadStatus.objects.all().order_by('-updated_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadStatusCreateSerializer
        return LeadStatusSerializer



# LeadSource ViewSet

class LeadSourceViewSet(viewsets.ModelViewSet):
    queryset = LeadSource.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadSourceCreateSerializer
        return LeadSourceSerializer



# LeadNote ViewSet

class LeadNoteViewSet(viewsets.ModelViewSet):
    queryset = LeadNote.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadNoteCreateSerializer
        return LeadNoteSerializer



# LeadActivity ViewSet
class LeadActivityViewSet(viewsets.ModelViewSet):
    queryset = LeadActivity.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadActivityCreateSerializer
        return LeadActivitySerializer



# LeadAssignment ViewSet

class LeadAssignmentViewSet(viewsets.ModelViewSet):
    queryset = LeadAssignment.objects.all().order_by('-assigned_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadAssignmentCreateSerializer
        return LeadAssignmentSerializer



# LeadTag ViewSet
class LeadTagViewSet(viewsets.ModelViewSet):
    queryset = LeadTag.objects.all().order_by('-id')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadTagCreateSerializer
        return LeadTagSerializer



# LeadCampaign ViewSet

class LeadCampaignViewSet(viewsets.ModelViewSet):
    queryset = LeadCampaign.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadCampaignCreateSerializer
        return LeadCampaignSerializer



# LeadConversion ViewSet

class LeadConversionViewSet(viewsets.ModelViewSet):
    queryset = LeadConversion.objects.all().order_by('-converted_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadConversionCreateSerializer
        return LeadConversionSerializer



# LeadFollowUp ViewSet

class LeadFollowUpViewSet(viewsets.ModelViewSet):
    queryset = LeadFollowUp.objects.all().order_by('follow_up_date')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadFollowUpCreateSerializer
        return LeadFollowUpSerializer



# LeadDocument ViewSet

class LeadDocumentViewSet(viewsets.ModelViewSet):
    queryset = LeadDocument.objects.all().order_by('-uploaded_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadDocumentCreateSerializer
        return LeadDocumentSerializer



# LeadPriority ViewSet

class LeadPriorityViewSet(viewsets.ModelViewSet):
    queryset = LeadPriority.objects.all().order_by('-set_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadPriorityCreateSerializer
        return LeadPrioritySerializer



# LeadReminder ViewSet

class LeadReminderViewSet(viewsets.ModelViewSet):
    queryset = LeadReminder.objects.all().order_by('reminder_date')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadReminderCreateSerializer
        return LeadReminderSerializer



# LeadScore ViewSet

class LeadScoreViewSet(viewsets.ModelViewSet):
    queryset = LeadScore.objects.all().order_by('-last_updated')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadScoreCreateSerializer
        return LeadScoreSerializer



# LeadCall ViewSet

class LeadCallViewSet(viewsets.ModelViewSet):
    queryset = LeadCall.objects.all().order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return LeadCallCreateSerializer
        return LeadCallSerializer