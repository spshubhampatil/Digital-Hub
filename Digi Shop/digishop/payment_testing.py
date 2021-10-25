from instamojo_wrapper import Instamojo
from digishop.settings import PAYMENT_API_KEY,PAYMENT_API_AUTH_TOKEN

api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

# Create a new Payment Request
response = api.payment_request_create(
    amount='20',
    purpose='Testing Payment',
    send_email=True,
    email="spshubhamspatil@gmail.com",
    redirect_url="http://127.0.0.1:8000/"
    )
# print the long URL of the payment request.
url=response['payment_request']['longurl']
print(url)