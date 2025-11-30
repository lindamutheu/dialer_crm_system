import logging
from django_conf import settings
from Intergrations.models import IntegrationLog
from django.utils.timezone import now
from django.core.mail import send_mail, EmailMessage


logger = logging.getLogger(__name__)

class EmailService:
    def send_email(self, to_email, subject, body):
        raise NotImplementedError("Subclasses must implement this method")

class SMTPEmailService(EmailService):
    def send_email(self, to_email, subject, body):
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [to_email],
                fail_silently=False,
            )
            IntegrationLog.objects.create(
                service_name="SMTP",
                action="Send Email",
                status="Success",
                details=f"Email sent to {to_email}",
                timestamp=now()
            )
            return True
        except Exception as e:
            logger.error(f"Failed to send email via SMTP: {e}")
            IntegrationLog.objects.create(
                service_name="SMTP",
                action="Send Email",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return False
        
class SendGridEmailService(EmailService):
    def send_email(self, to_email, subject, body):
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        message = Mail(
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_emails=to_email,
            subject=subject,
            plain_text_content=body
        )
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            if response.status_code in [200, 202]:
                IntegrationLog.objects.create(
                    service_name="SendGrid",
                    action="Send Email",
                    status="Success",
                    details=f"Email sent to {to_email}",
                    timestamp=now()
                )
                return True
            else:
                raise Exception(f"SendGrid API returned status code {response.status_code}")
        except Exception as e:
            logger.error(f"Failed to send email via SendGrid: {e}")
            IntegrationLog.objects.create(
                service_name="SendGrid",
                action="Send Email",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return False

def get_email_service(service_name):
    if service_name == "SMTP":
        return SMTPEmailService()
    elif service_name == "SendGrid":
        return SendGridEmailService()
    else:
        raise ValueError(f"Unsupported email service: {service_name}")
    
    