import logging
from intergrations.models import IntegrationLog
from django.utils.timezone import now

logger = logging.getLogger(__name__)

class PaymentService:
    def process_payment(self, amount, currency, payment_method):
        raise NotImplementedError("Subclasses must implement this method")

class StripePaymentService(PaymentService):
    def process_payment(self, amount, currency, payment_method):
        import stripe
        stripe.api_key = "your_stripe_api_key"

        try:
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # amount in cents
                currency=currency,
                source=payment_method,
                description="CRM Payment"
            )
            IntegrationLog.objects.create(
                service_name="Stripe",
                action="Process Payment",
                status="Success",
                details=f"Charge ID: {charge.id}",
                timestamp=now()
            )
            return charge
        except Exception as e:
            logger.error(f"Failed to process payment via Stripe: {e}")
            IntegrationLog.objects.create(
                service_name="Stripe",
                action="Process Payment",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return None
    
class PayPalPaymentService(PaymentService):
    def process_payment(self, amount, currency, payment_method):
        import paypalrestsdk
        paypalrestsdk.configure({
            "mode": "sandbox",  # or "live"
            "client_id": "your_client_id",
            "client_secret": "your_client_secret"
        })

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": f"{amount:.2f}",
                    "currency": currency
                },
                "description": "CRM Payment"
            }],
            "redirect_urls": {
                "return_url": "http://localhost:8000/payment/execute",
                "cancel_url": "http://localhost:8000/payment/cancel"
            }
        })

        try:
            if payment.create():
                IntegrationLog.objects.create(
                    service_name="PayPal",
                    action="Process Payment",
                    status="Success",
                    details=f"Payment ID: {payment.id}",
                    timestamp=now()
                )
                return payment
            else:
                raise Exception(payment.error)
        except Exception as e:
            logger.error(f"Failed to process payment via PayPal: {e}")
            IntegrationLog.objects.create(
                service_name="PayPal",
                action="Process Payment",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return None
        
class ChapaPaymentService(PaymentService):
    def process_payment(self, amount, currency, payment_method):
        import requests

        url = "https://api.chapa.co/v1/transaction/initialize"
        headers = {
            "Authorization": "Bearer your_chapa_api_key",
            "Content-Type": "application/json"
        }
        data = {
            "amount": amount,
            "currency": currency,
            "email": payment_method,  # assuming payment_method is email for Chapa
            "callback_url": "http://localhost:8000/payment/callback"
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response_data = response.json()
            if response.status_code == 200 and response_data.get("status") == "success":
                IntegrationLog.objects.create(
                    service_name="Chapa",
                    action="Process Payment",
                    status="Success",
                    details=f"Transaction ID: {response_data['data']['id']}",
                    timestamp=now()
                )
                return response_data
            else:
                raise Exception(response_data.get("message", "Unknown error"))
        except Exception as e:
            logger.error(f"Failed to process payment via Chapa: {e}")
            IntegrationLog.objects.create(
                service_name="Chapa",
                action="Process Payment",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return None
        
class PaystackPaymentService(PaymentService):
    def process_payment(self, amount, currency, payment_method):
        import requests

        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": "Bearer your_paystack_api_key",
            "Content-Type": "application/json"
        }
        data = {
            "amount": int(amount * 100),  # amount in kobo
            "email": payment_method,  # assuming payment_method is email for Paystack
            "currency": currency,
            "callback_url": "http://localhost:8000/payment/callback"
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response_data = response.json()
            if response.status_code == 200 and response_data.get("status") is True:
                IntegrationLog.objects.create(
                    service_name="Paystack",
                    action="Process Payment",
                    status="Success",
                    details=f"Transaction Reference: {response_data['data']['reference']}",
                    timestamp=now()
                )
                return response_data
            else:
                raise Exception(response_data.get("message", "Unknown error"))
        except Exception as e:
            logger.error(f"Failed to process payment via Paystack: {e}")
            IntegrationLog.objects.create(
                service_name="Paystack",
                action="Process Payment",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return None
        
class MpesaPaymentService(PaymentService):
    def process_payment(self, amount, currency, payment_method):
        import requests

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {
            "Authorization": "Bearer your_mpesa_access_token",
            "Content-Type": "application/json"
        }
        data = {
            "BusinessShortCode": "your_shortcode",
            "Password": "generated_password",
            "Timestamp": "generated_timestamp",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": payment_method,  # assuming payment_method is phone number for M-Pesa
            "PartyB": "your_shortcode",
            "PhoneNumber": payment_method,
            "CallBackURL": "http://localhost:8000/payment/callback",
            "AccountReference": "CRM Payment",
            "TransactionDesc": "Payment for CRM services"
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response_data = response.json()
            if response.status_code == 200 and response_data.get("ResponseCode") == "0":
                IntegrationLog.objects.create(
                    service_name="M-Pesa",
                    action="Process Payment",
                    status="Success",
                    details=f"Checkout Request ID: {response_data['CheckoutRequestID']}",
                    timestamp=now()
                )
                return response_data
            else:
                raise Exception(response_data.get("errorMessage", "Unknown error"))
        except Exception as e:
            logger.error(f"Failed to process payment via M-Pesa: {e}")
            IntegrationLog.objects.create(
                service_name="M-Pesa",
                action="Process Payment",
                status="Failure",
                details=str(e),
                timestamp=now()
            )
            return None
        
def get_payment_service(service_name):
    if service_name == "Stripe":
        return StripePaymentService()
    elif service_name == "PayPal":
        return PayPalPaymentService()
    elif service_name == "Chapa":
        return ChapaPaymentService()
    elif service_name == "Paystack":
        return PaystackPaymentService()
    elif service_name == "Mpesa":
        return MpesaPaymentService()
    else:
        raise ValueError(f"Unsupported payment service: {service_name}")
    

