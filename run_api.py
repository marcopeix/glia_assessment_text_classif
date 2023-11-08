import requests
import json

headers={
    'Content-type':'application/json', 
    'Accept':'application/json',
    'Accept-Charset': 'UTF-8'
}

sample_text = 'Add this song to my playlist'

payload = json.dumps([sample_text])
print(payload)

r = requests.post('http://127.0.0.1:5000/predict', data=payload, headers=headers)

print(r.text)