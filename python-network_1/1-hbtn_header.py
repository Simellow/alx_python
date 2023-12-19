"""" """
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
    print(f"The value of X-Request-Id in the response header is: {request_id}")
