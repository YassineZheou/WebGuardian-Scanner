def check_headers(headers):

    print("\nChecking security headers...\n")

    security_headers = {
        "Content-Security-Policy": "Protects against XSS attacks",
        "X-Frame-Options": "Prevents clickjacking",
        "X-XSS-Protection": "XSS filter",
        "Strict-Transport-Security": "Forces HTTPS"
    }

    for header, description in security_headers.items():

        if header in headers:
            print("[+] {} found".format(header))
        else:
            print("[!] {} missing".format(header))
