import requests
import json

url = 'http://0.0.0.0:8080/process_image'
files = {'image': open('test2.png', 'rb')}

r = requests.post(url, files=files)

print(r.text)

list_smi = json.loads(r.text)
for smi in list_smi:
    print(smi)