"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import requests
import sys

if __name__ == '__main__':
    with requests.urlopen(sys.argv[1]) as response:
        print("{}".format(response.getheader('X-Request-Id')))
