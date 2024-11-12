import sys
from core import xst_checker, host_header_injection_checker, clickjacking_checker, cors_checker

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    LIGHT_GRAY = '\033[90m'
    DARK_GRAY = '\033[90m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_RED = '\033[91m'
    LIGHT_YELLOW = '\033[93m'

def main(argv):
    argc = len(argv)

    if argc <= 2:
        print(bcolors.LIGHT_YELLOW + "  _   _  _  _  ___  ___   " + bcolors.ENDC)
        print(bcolors.LIGHT_GRAY+ " ( )_( )( \/ )/ __)/ __)  " + bcolors.ENDC)
        print(bcolors.LIGHT_YELLOW + "  ) _ (  )  (( (__( (__   " + bcolors.ENDC)
        print(bcolors.LIGHT_GRAY + " (_) (_)(_/\_)\___)\___)  " + bcolors.ENDC)
        print(bcolors.OKBLUE + "                               " + bcolors.ENDC)
        print(bcolors.PURPLE + "  HXCC - The HTTP Vulnerability Checker" + bcolors.ENDC)
        print(bcolors.PURPLE + "  by @Zierax v1.0" + bcolors.ENDC)
        print(bcolors.OKGREEN + "  usage: %s <host> <port>" % (argv[0]) + bcolors.ENDC)
        sys.exit(0)

    target = argv[1]
    port = int(argv[2])

    print(bcolors.OKBLUE + "+ -- --=[Scanning " + target + " on port " + str(port) + " for vulnerabilities..." + bcolors.ENDC)

    xst_result = xst_checker.check_xst(target, port)
    host_header_injection_result = host_header_injection_checker.check_host_header_injection(target, port)
    clickjacking_result = clickjacking_checker.check_clickjacking(target, port)
    cors_result = cors_checker.check_cors(target, port)

    print(bcolors.OKGREEN + "XST Check: " + (bcolors.BOLD + bcolors.FAIL + "Vulnerable" if xst_result else "Not Vulnerable") + bcolors.ENDC)
    print(bcolors.OKGREEN + "Host Header Injection Check: " + (bcolors.BOLD + bcolors.FAIL + "Vulnerable" if host_header_injection_result else "Not Vulnerable") + bcolors.ENDC)
    print(bcolors.OKGREEN + "Clickjacking Check: " + (bcolors.BOLD + bcolors.FAIL + "Vulnerable" if clickjacking_result else "Not Vulnerable") + bcolors.ENDC)
    print(bcolors.OKGREEN + "CORS Check: " + (bcolors.BOLD + bcolors.FAIL + "Vulnerable" if cors_result else "Not Vulnerable") + bcolors.ENDC)

if __name__ == "__main__":
    main(sys.argv)