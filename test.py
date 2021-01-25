import requests

url = 'http://0.0.0.0:80/process_image'
files = {'image': open('test2.png', 'rb')}

r = requests.post(url, files=files)

print(r.text)