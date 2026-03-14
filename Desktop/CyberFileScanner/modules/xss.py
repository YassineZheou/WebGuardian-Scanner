import requests

def test_xss(url):

    payload = "<script>alert(1)</script>"

    test_url = url + "?q=" + payload

    response = requests.get(test_url)

    if payload in response.text:
        print("[!] Possible XSS vulnerability")
    else:
        print("[+] XSS not detected")
