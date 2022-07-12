
import requests
import  keys
from access_token import generate_access_token
access_token = generate_access_token()

def register_c2b():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}

    options = {"ShortCode": keys.ShortCode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://127.0.0.1:8000/api/v1/c2b/confirmation/",
               "ValidationURL": "https://127.0.0.1:8000/api/v1/c2b/validation/"}

    response = requests.post(api_url, json=options, headers=headers)

    print(response.text)

register_c2b()

def simulate_c2b_transaction():
    my_access_token = access_token

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": keys.ShortCode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "4",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber": "myaccnumber",
    }
    try:
        response = requests.post(api_url, json=request, headers=headers)

    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)


simulate_c2b_transaction()