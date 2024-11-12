import requests

def check_host_header_injection(target, port):
    try:
        response = requests.get(f"http://{target}:{port}/", headers={'Host': 'http://evil.com', 'X-Forwarded-Host': 'http://evil.com'}, timeout=1)
        if "evil" in response.text:
            return True
    except requests.exceptions.Timeout:
        print(f"Timeout connecting to {target}:{port}")
    except requests.exceptions.ConnectionError:
        print(f"Failed to connect to {target}:{port}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return False