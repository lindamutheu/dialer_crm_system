from rest_framework import viewsets, permissions
from .models import (
    Call, CallQueue, CallSchedule, CallDisposition,
    CallStatistic, CallCampaign, CampaignCall,
    AgentStatus, CallRecording
)
from .serializers import (
    CallSerializer, CallCreateSerializer,
    CallQueueSerializer, CallQueueCreateSerializer,
    CallScheduleSerializer, CallScheduleCreateSerializer,
    CallDispositionSerializer, CallDispositionCreateSerializer,
    CallStatisticSerializer, CallStatisticCreateSerializer,
    CallCampaignSerializer,
    CampaignCallSerializer, CampaignCallCreateSerializer,
    AgentStatusSerializer, AgentStatusCreateSerializer,
    CallRecordingSerializer, CallRecordingCreateSerializer
)


# ---------------------------
# Call ViewSet
# ---------------------------
class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CallCreateSerializer
        return CallSerializer

    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# CallQueue ViewSet
# ---------------------------
class CallQueueViewSet(viewsets.ModelViewSet):
    queryset = CallQueue.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CallQueueCreateSerializer
        return CallQueueSerializer

    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# CallSchedule ViewSet
# ---------------------------
class CallScheduleViewSet(viewsets.ModelViewSet):
    queryset = CallSchedule.objects.all().order_by('scheduled_time')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CallScheduleCreateSerializer
        return CallScheduleSerializer

    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# CallDisposition ViewSet
# ---------------------------
class CallDispositionViewSet(viewsets.ModelViewSet):
    queryset = CallDisposition.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CallDispositionCreateSerializer
        return CallDispositionSerializer

    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# CallStatistic ViewSet
# ---------------------------
class CallStatisticViewSet(viewsets.ModelViewSet):
    queryset = CallStatistic.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CallStatisticCreateSerializer
        return CallStatisticSerializer

    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# CallCampaign ViewSet
# ---------------------------
class CallCampaignViewSet(viewsets.ModelViewSet):
    queryset = CallCampaign.objects.all().order_by('-start_date')
    serializer_class = CallCampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# CampaignCall ViewSet
# ---------------------------
class CampaignCallViewSet(viewsets.ModelViewSet):
    queryset = CampaignCall.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CampaignCallCreateSerializer
        return CampaignCallSerializer

    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# AgentStatus ViewSet
# ---------------------------
class AgentStatusViewSet(viewsets.ModelViewSet):
    queryset = AgentStatus.objects.all().order_by('-last_updated')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AgentStatusCreateSerializer
        return AgentStatusSerializer

    permission_classes = [permissions.IsAuthenticated]


# ---------------------------
# CallRecording ViewSet
# ---------------------------
class CallRecordingViewSet(viewsets.ModelViewSet):
    queryset = CallRecording.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CallRecordingCreateSerializer
        return CallRecordingSerializer

    permission_classes = [permissions.IsAuthenticated]
