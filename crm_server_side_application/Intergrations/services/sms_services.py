from django.conf import settings
from Intergrations.models import IntegrationLog
from django.utils.timezone import now
import logging


logger = logging.getLogger(__name__)


class SMSService:
    def send_sms(self, to_number, message):
        raise NotImplementedError("Subclasses must implement this method")


class TwilioSMSService(SMSService):
    def send_sms(self, to_number, message):
        from twilio.rest import Client

        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        try:
            sms = client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=to_number
            )
            IntegrationLog.objects.create(
                service_name="Twilio",
                action="Send SMS",
                status="Success",
                details=f"Message SID: {sms.sid}",
                timestamp=now()
            )
            return sms.sid
        except Exception as e:
            logger.error(f"Failed to send SMS via Twilio: {e}")
            IntegrationLog.objects.create(
                service_name="Twilio",
                action="Send SMS",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return None
        

class NexmoSMSService(SMSService):
    def send_sms(self, to_number, message):
        import vonage

        client = vonage.Client(key=settings.NEXMO_API_KEY, secret=settings.NEXMO_API_SECRET)
        sms = vonage.Sms(client)

        responseData = sms.send_message(
            {
                "from": settings.NEXMO_FROM_NUMBER,
                "to": to_number,
                "text": message,
            }
        )

        if responseData["messages"][0]["status"] == "0":
            IntegrationLog.objects.create(
                service_name="Nexmo",
                action="Send SMS",
                status="Success",
                details=f"Message ID: {responseData['messages'][0]['message-id']}",
                timestamp=now()
            )
            return responseData['messages'][0]['message-id']
        else:
            error_text = responseData["messages"][0]["error-text"]
            logger.error(f"Failed to send SMS via Nexmo: {error_text}")
            IntegrationLog.objects.create(
                service_name="Nexmo",
                action="Send SMS",
                status="Failure",
                details=error_text,
                timestamp=now()
            )
            return None
        
def get_sms_service(service_name):
    if service_name == "Twilio":
        return TwilioSMSService()
    elif service_name == "Nexmo":
        return NexmoSMSService()
    else:
        raise ValueError(f"Unsupported SMS service: {service_name}")
    

