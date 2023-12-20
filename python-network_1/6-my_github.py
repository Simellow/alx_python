"""CHECK"""
import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = "https://api.github.com/user"
response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    user_id = response.json()["id"]
    print("User ID:", user_id)
else:
    print("Failed to retrieve user ID. Please check your credentials.")