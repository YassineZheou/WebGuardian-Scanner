from colorama import Fore

def server_info(headers):

    if "Server" in headers:
        print(Fore.GREEN + "[+] Server:", headers["Server"])

    if "X-Powered-By" in headers:
        print(Fore.GREEN + "[+] Technology:", headers["X-Powered-By"])
