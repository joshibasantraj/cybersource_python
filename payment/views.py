from django.shortcuts import render
from django.http import HttpResponse
import uuid
import datetime
import pprint
import hmac
import hashlib,base64
import requests
from django.utils import timezone

# Create your views here.



def home(request):
    now = timezone.now()
    datetimestr = datetime.datetime.strftime(now, "%Y-%m-%dT%H:%M:%SZ")
    
    data = {
        'access_key':'fced28c8d9953a0ea812c6b12a02826b',
        'profile_id':'2198A976-3F7E-46BC-8FA4-759C8459F202',
        'transaction_uuid':str(uuid.uuid4()),
        # 'signed_date_time':datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
         'signed_date_time':datetimestr
    }
    return render(request,'home.html',data)

# def confirm(request):
#     # import pdb; pdb.set_trace();
#     amount = request.POST.items()
#     return HttpResponse(amount)


def confirm(request):
    data = {}
    for k,v in request.POST.items():
        data[k]=v
    
    signed_field_names = request.POST['signed_field_names']
    field_array = signed_field_names.split(',')
    field_values = []
    for key in field_array:
        field_values.append("{}={}".format(key,request.POST[key]))
    field_string = ",".join(field_values)
    hashValue = hmac.new("0267caf548c44c42a736bbd6ad74ece98168c8c7875f40af966f127ced89ed82a169c6ddb2db4eb4895d6a64a432ae3f4b7ae46d536741e7bf00474e29e2f62a33e65932d11746ddad0ca473c226de0d22c677cda3884aab9f4f1b50681a69f4dfb28fbd45504b08a20ca0e8be6a91bae0fe24188c34444785d94932c0340a88".encode(),field_string.encode(),hashlib.sha256).digest()
    hashValue = base64.b64encode(hashValue)
    data.pop('csrfmiddlewaretoken')
    data['signature'] = hashValue.decode()
    # import pdb; pdb.set_trace();
    # url = 'https://testsecureacceptance.cybersource.com/pay'
    # response = requests.post(url,data)
    # print(response.json())
   
    return render(request,'confirm.html',{'data':data})




    
    # return HttpResponse(data['signature']) 
    

# def payload(request):
#     data = {  
#             'access_key': 'fced28c8d9953a0ea812c6b12a02826b',
#             'profile_id': '2198A976-3F7E-46BC-8FA4-759C8459F202',
#             'transaction_uuid': '549dfad1-2496-4b4d-aa7e-1a06e0ae4f50',
#             'signed_field_names': 'access_key,profile_id,transaction_uuid,signed_field_names,unsigned_field_names,signed_date_time,locale,transaction_type,reference_number,amount,currency,payment_method,bill_to_forename,bill_to_surname,bill_to_email,bill_to_phone,bill_to_address_line1,bill_to_address_city,bill_to_address_state,bill_to_address_country,bill_to_address_postal_code',
#             'unsigned_field_names': 'card_type,card_number,card_expiry_date',
#             'signed_date_time': '2022-08-25T04:22:27Z',
#             'locale': 'en',
#             'auth_trans_ref_no': '',
#             'bill_to_forename': 'Basant',
#             'bill_to_surname': 'Joshi',
#             'bill_to_email': 'joshibasantraj@gmail.com',
#             'bill_to_phone': '9742395923',
#             'bill_to_address_line1': 'Kathmandu',
#             'bill_to_address_city': 'Kathmandu',
#             'bill_to_address_state': 'Kathmandu',
#             'bill_to_address_country': 'NP',
#             'bill_to_address_postal_code': 'Kathmandu',
#             'amount': '1',
#             'transaction_type': 'sale',
#             'reference_number': '609',
#             'currency': 'NPR',
#             'payment_method': 'card',
#             'card_type': '001',
#             'card_number':'', 
#             'card_expiry_date':'', 
#             'signature': 'BBHYeSVq/A0CispnfyHpw8PU31PNKsouxVdCUVodVOQ='     
#     }                                        