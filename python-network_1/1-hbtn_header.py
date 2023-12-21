# """CHECK"""
# import requests
# import sys

# url = sys.argv[1]
# response = requests.get(url)

# x_request_id = response.headers.get('X-Request-Id')
# print("X-Request-Id:", x_request_id)


# """ takes a URL, sends a request and returns"""


# import urllib.request
# import sys

# if __name__ == '__main__':
#     with urllib.request.urlopen(sys.argv[1]) as response:
#         print("{}".format(response.getheader('X-Request-Id')))

"""check"""
import requests
import sys

def get_request_id(url):
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    return request_id

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
        sys.exit(1)

    url = sys.argv[1]
    request_id = get_request_id(url)
    print(request_id)

