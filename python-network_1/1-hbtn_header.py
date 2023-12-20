"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)

x_request_id = response.headers.get('X-Request-Id')
print("X-Request-Id:", x_request_id)

