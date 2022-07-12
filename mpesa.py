
import requests
import keys
from datetime import datetime
from access_token import generate_access_token
from encode import generate_password
from utils import get_timestamp

def lipanampesa():
    mytoken=generate_access_token()
    # formatted_time=get_timestamp()
    # decoded_password=generate_password(formatted_time)

    headers = {
      'Content-Type': 'application/json',

      "Authorization": "Bearer %s" % mytoken
    }


    payload = {
        "BusinessShortCode": keys.business_code,
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwOTI1MjIzNTAx",
        "Timestamp": "20210925223501",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": keys.phonenumber,
        "PartyB": keys.business_code,
        "PhoneNumber": keys.phonenumber,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    }

    response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',json = payload, headers = headers )

    print(response.text.encode('utf8'))

lipanampesa()