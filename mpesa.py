
import requests
import keys

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer XiB6TQfYSgmPAbDGbwsOfAs6ccjU'
}


payload = {
    "BusinessShortCode": keys.business_code,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjEwOTI1MjIzNTAx",
    "Timestamp": "20210925223501",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": keys.phonenumber,
    "PartyB": 174379,
    "PhoneNumber": keys.phonenumber,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X"
}

response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',json = payload, headers = headers )

print(response.text.encode('utf8'))
# print(response.text)