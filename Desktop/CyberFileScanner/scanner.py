import requests
import sys
from colorama import Fore

from modules.headers import check_headers
from modules.info import server_info
from modules.forms import get_forms
from modules.xss import test_xss
from modules.sql import test_sql


def scan_site(url):

    print(Fore.CYAN + "\n========== WEB SECURITY SCANNER ==========\n")

    try:
        response = requests.get(url, timeout=10)

        print(Fore.YELLOW + "Target:", url)
        print("Status:", response.status_code)
        print("Final URL:", response.url)

        print("\n--- Server Information ---")
        server_info(response.headers)

        print("\n--- Security Headers ---")
        check_headers(response.headers)

        print("\n--- Form Detection ---")
        forms = get_forms(url)

        print("\n--- XSS Test ---")
        test_xss(url)

        print("\n--- SQL Injection Test ---")
        test_sql(url)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + "Error:", e)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python scanner.py https://site.com")
        sys.exit()

    url = sys.argv[1]

    scan_site(url)
