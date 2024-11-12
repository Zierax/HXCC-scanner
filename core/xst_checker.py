import socket

def check_xst(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        s.connect((target, port))
        s.sendall(b"TRACE / HTTP/1.1\r\nVia: '><script>prompt(evil);</script>\r\nHost: " + target.encode() + b"\r\n\r\n")
        data = s.recv(1024).decode()
        s.close()
        if "'><script>prompt(evil);</script>" in data:
            return True
    except Exception as e:
        print(f"Error checking XST: {e}")
    return False