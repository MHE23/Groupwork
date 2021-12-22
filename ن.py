

import requests

pr = {'receptor':['09912512389','09121440015','09129479799'],'message':'مشترک گرامی درحساب شمایه مبلق 10000000 ریال واریز شد ','sender':'10004346'}
url = 'https://api.kavenegar.com/v1/{6B5244766C32486A30426356624439756178306245323752654A762F354D3937465546456E4E3467364E413D}/sms/pr.json'

api = requests.post(url,data=pr)
print(api)



