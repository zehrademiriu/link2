import requests
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system('cls' if os.name == 'nt' else 'clear')

url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

payload={}
headers = {}

print(bcolors.OKCYAN + "Scraping proxies..." + bcolors.ENDC)

response = requests.request("GET", url, headers=headers, data=payload)

file = open("proxylist.txt", "w")
file.write(response.text)
file.close

print(bcolors.OKGREEN + "Scraping complete. Proxy list saved to proxylist.txt" + bcolors.ENDC)