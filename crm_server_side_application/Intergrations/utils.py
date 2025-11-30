import json
import django_conf as settings
from django.apps import AppConfig

def get_payment_service(service_name):
    if service_name == "PayPal":
        from Intergrations.services.payment_services import PayPalPaymentService
        return PayPalPaymentService()
    elif service_name == "Chapa":
        from Intergrations.services.payment_services import ChapaPaymentService
        return ChapaPaymentService()
    else:
        raise ValueError(f"Unsupported payment service: {service_name}")

def get_email_service(service_name):
    if service_name == "SMTP":
        from Intergrations.services.email_services import SMTPEmailService
        return SMTPEmailService()
    elif service_name == "SendGrid":
        from Intergrations.services.email_services import SendGridEmailService
        return SendGridEmailService()
    else:
        raise ValueError(f"Unsupported email service: {service_name}")
    
def get_sms_service(service_name):
    if service_name == "Twilio":
        from Intergrations.services.sms_services import TwilioSMSService
        return TwilioSMSService()
    elif service_name == "Nexmo":
        from Intergrations.services.sms_services import NexmoSMSService
        return NexmoSMSService()
    else:
        raise ValueError(f"Unsupported SMS service: {service_name}")
    

def get_integration_log_details(log):
    try:
        return json.loads(log.details)
    except json.JSONDecodeError:
        return {"message": log.details}
    
