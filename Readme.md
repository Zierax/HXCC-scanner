# HXCC - HTTP Vulnerability Checker

HXCC is a simple yet powerful tool designed to scan web applications for common HTTP vulnerabilities. It's written in Python and utilizes the `requests` and `socket` libraries for network communication.

## Features

* **Cross-Site Tracing (XST) Detection:** Checks for vulnerabilities related to the `TRACE` HTTP method, which can be exploited to inject malicious scripts.
* **Host Header Injection Detection:** Detects if the application is vulnerable to host header injection, allowing attackers to manipulate the server's perceived origin.
* **Clickjacking Detection:** Identifies if the application lacks proper security headers (like `X-Frame-Options` or `Content-Security-Policy`) to prevent clickjacking attacks.
* **CORS (Cross-Origin Resource Sharing) Policy Analysis:** Analyzes the CORS policy of the application to determine if it allows access from potentially malicious origins.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/HXCC.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd HXCC
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
```

bash
python main.py <target_host> <target_port>

```
## Output

The tool will print the results of each vulnerability check in a clear and concise format:

```
+ -- --=[Scanning example.com on port 80 for vulnerabilities...
XST Check: Not Vulnerable
Host Header Injection Check: Vulnerable
Clickjacking Check: Not Vulnerable
CORS Check: Vulnerable

```


## Contributing

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new vulnerability checks, feel free to open an issue or submit a pull request.

## Disclaimer

This tool is intended for educational purposes only. It should not be used to scan or exploit systems without the owner's explicit permission. Use this tool responsibly and ethically.