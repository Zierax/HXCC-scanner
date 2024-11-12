import requests

def check_cors(target, port, origin='http://evil.com'):
    url = f"http://{target}:{port}/"
    cors_headers = [
        'Access-Control-Allow-Origin',
        'Access-Control-Allow-Methods',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Credentials'
    ]
    
    try:
        # Send an OPTIONS request to check the CORS policy
        response = requests.options(url, headers={'Origin': origin}, timeout=5)
        
        # Check if the CORS headers are present in the response
        cors_found = {header: response.headers.get(header) for header in cors_headers}
        
        # Check if the CORS policy allows access from the evil domain
        if 'Access-Control-Allow-Origin' in response.headers:
            allow_origin = response.headers['Access-Control-Allow-Origin']
            # If the CORS header is *, allow all origins
            if allow_origin == '*':
                return True
            # If the specific origin is allowed, check for credentials
            elif allow_origin == origin:
                if 'Access-Control-Allow-Credentials' in response.headers:
                    return True
        # If no relevant CORS headers or permissions found
        return False
    except requests.exceptions.RequestException as e:
        # Handle request exceptions (timeouts, connection issues, etc.)
        return False