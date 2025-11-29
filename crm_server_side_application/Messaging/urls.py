from rest_framework.routers import DefaultRouter
from .serializers import MessageSerializer, MessageReactionSerializer, MessageReadReceiptSerializer, UserPresenceSerializer, ConversationSerializer, ConversationMemberSerializer, AttachmentSerializer, ScheduledMessageSerializer, AutoResponderSerializer, MessageQueueSerializer, MessageTemplateUsageSerializer, MessageForwardingSerializer
from rest_framework import routers
from .models import Message, MessageReaction, MessageReadReceipt, UserPresence, Conversation, ConversationMember, Attachment, ScheduledMessage, AutoResponder, MessageQueue, MessageTemplateUsage, MessageForwarding  
from .views import MessageViewSet, MessageReactionViewSet, MessageReadReceiptViewSet, UserPresenceViewSet, ConversationViewSet, ConversationMemberViewSet, AttachmentViewSet, ScheduledMessageViewSet, AutoResponderViewSet, MessageQueueViewSet, MessageTemplateUsageViewSet, MessageForwardingViewSet

router = DefaultRouter()

router.register("messages", MessageViewSet)
router.register("reactions", MessageReactionViewSet)
router.register("read-receipts", MessageReadReceiptViewSet)
router.register("presence", UserPresenceViewSet)
router.register("conversations", ConversationViewSet)
router.register("conversation-members", ConversationMemberViewSet)
router.register("attachments", AttachmentViewSet)
router.register("scheduled-messages", ScheduledMessageViewSet)
router.register("autoresponders", AutoResponderViewSet)
router.register("queue", MessageQueueViewSet)
router.register("template-usage", MessageTemplateUsageViewSet)
router.register("forwarding", MessageForwardingViewSet)

urlpatterns = router.urls
