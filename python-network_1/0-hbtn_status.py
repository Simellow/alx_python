# """ """
# import requests
# """ """
# url = "https://alu-intranet.hbtn.io/status"
# """ """
# requests.get(url)
#!/usr/bin/python3
# import requests

# url = "https://alu-intranet.hbtn.io/status"
# response = requests.get(url)
"""nknk"""
import urllib.request as req
if __name__ == "__main__":
    with req.urlopen('https://alu-intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
