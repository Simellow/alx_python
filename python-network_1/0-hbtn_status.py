"""importing requests module"""
import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

print(response)

# Body response:$
#     - type: <class 'str'>$
#     - content: OK$
