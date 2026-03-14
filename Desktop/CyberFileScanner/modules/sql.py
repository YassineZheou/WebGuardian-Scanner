import requests

def test_sql(url):

    payload = "'"

    test_url = url + "?id=" + payload

    response = requests.get(test_url)

    errors = [
        "SQL syntax",
        "mysql_fetch",
        "ORA-01756",
        "SQL error"
    ]

    for error in errors:
        if error in response.text:
            print("[!] Possible SQL Injection")
            return

    print("[+] SQL injection not detected")
