import requests 

url = "http://localhost:8899"

req = requests.get(url)
print("Status code:",req.status_code)

#msg = req.json()
#msg = req.text
msg = req.content
print(msg)