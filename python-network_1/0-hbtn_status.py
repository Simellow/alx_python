"""importing requests module"""
import requests

response = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
# import requests

# url = "https://alu-intranet.hbtn.io/status"

# response = requests.get(url)

# print(response)

# Body response:$
#     - type: <class 'str'>$
#     - content: OK$
