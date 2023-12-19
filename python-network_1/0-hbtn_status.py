# """ """
# import requests
# """ """
# url = "https://alu-intranet.hbtn.io/status"
# """ """
# requests.get(url)
#!/usr/bin/python3
import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    print("Body response:")
    for line in response.text.splitlines():
        print("\t- " + line)
else:
    print("Error: Failed to fetch the URL. Status code:", response.status_code)

