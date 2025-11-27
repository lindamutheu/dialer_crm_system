from rest_framework import routers
from .viewsets import (
    CallViewSet, CallQueueViewSet, CallScheduleViewSet, CallDispositionViewSet,
    CallStatisticViewSet, CallCampaignViewSet, CampaignCallViewSet,
    AgentStatusViewSet, CallRecordingViewSet
)

router = routers.DefaultRouter()
router.register(r'calls', CallViewSet)
router.register(r'queues', CallQueueViewSet)
router.register(r'schedules', CallScheduleViewSet)
router.register(r'dispositions', CallDispositionViewSet)
router.register(r'statistics', CallStatisticViewSet)
router.register(r'campaigns', CallCampaignViewSet)
router.register(r'campaign-calls', CampaignCallViewSet)
router.register(r'agents-status', AgentStatusViewSet)
router.register(r'recordings', CallRecordingViewSet)

urlpatterns = router.urls
