from bs4 import BeautifulSoup
import requests

def get_forms(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    forms = soup.find_all("form")

    print("[+] Found", len(forms), "forms")

    return forms
