import socket

def check_clickjacking(target, port, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"):

    buffer1 = "GET / HTTP/1.1"
    buffer2 = f"Host: {target}"
    buffer3 = f"User-Agent: {user_agent}"
    buffer4 = "Connection: close"  # Ensures the connection closes after response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)  # Increased timeout for slower responses
    try:
        # Try connecting to the target
        result = s.connect_ex((target, port))
        if result != 0:
            return False

        # Send HTTP request
        s.send(f"{buffer1}\r\n".encode())
        s.send(f"{buffer2}\r\n".encode())
        s.send(f"{buffer3}\r\n".encode())
        s.send(f"{buffer4}\r\n\r\n".encode())

        # Receive response
        data = s.recv(4096).decode()
        s.close()

        # Check for presence of headers to prevent clickjacking
        if "X-Frame-Options" not in data and "Content-Security-Policy" not in data:
            return True
        else:
            return False

    except socket.error as e:
        return False
