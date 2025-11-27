from rest_framework import routers
from .viewsets import (
    LeadViewSet, LeadStatusViewSet, LeadSourceViewSet, LeadNoteViewSet,
    LeadActivityViewSet, LeadAssignmentViewSet, LeadTagViewSet,
    LeadCampaignViewSet, LeadConversionViewSet, LeadFollowUpViewSet,
    LeadDocumentViewSet, LeadPriorityViewSet, LeadReminderViewSet,
    LeadScoreViewSet, LeadCallViewSet
)


router = routers.DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'lead-statuses', LeadStatusViewSet)
router.register(r'lead-sources', LeadSourceViewSet)
router.register(r'lead-notes', LeadNoteViewSet)
router.register(r'lead-activities', LeadActivityViewSet)
router.register(r'lead-assignments', LeadAssignmentViewSet)
router.register(r'lead-tags', LeadTagViewSet)
router.register(r'lead-campaigns', LeadCampaignViewSet)
router.register(r'lead-conversions', LeadConversionViewSet)
router.register(r'lead-follow-ups', LeadFollowUpViewSet)
router.register(r'lead-documents', LeadDocumentViewSet)
router.register(r'lead-priorities', LeadPriorityViewSet)
router.register(r'lead-reminders', LeadReminderViewSet)
router.register(r'lead-scores', LeadScoreViewSet)
router.register(r'lead-calls', LeadCallViewSet)

urlpatterns = router.urls
