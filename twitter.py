import requests
import time
import os
from proxy import workingProxy
from multiprocessing import Pool, Process, freeze_support, set_start_method, get_context

os.system('cls' if os.name == 'nt' else 'clear')

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

print(bcolors.OKCYAN + """
 ▄███▄   █▀▄▀█ ██   ▄█ █                         
 █▀   ▀  █ █ █ █ █  ██ █                         
 ██▄▄    █ ▄ █ █▄▄█ ██ █                         
 █▄   ▄▀ █   █ █  █ ▐█ ███▄                      
 ▀███▀      █     █  ▐     ▀                     
           ▀     █                               
                ▀                                
 ▄█▄     ▄  █ ▄███▄   ▄█▄    █  █▀ ▄███▄   █▄▄▄▄ 
 █▀ ▀▄  █   █ █▀   ▀  █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀ 
 █   ▀  ██▀▀█ ██▄▄    █   ▀  █▀▄   ██▄▄    █▀▀▌  
 █▄  ▄▀ █   █ █▄   ▄▀ █▄  ▄▀ █  █  █▄   ▄▀ █  █  
 ▀███▀     █  ▀███▀   ▀███▀    █   ▀███▀     █   
          ▀                   ▀             ▀    
                                                 
""" + bcolors.ENDC)

print(bcolors.OKCYAN + """
[ GitHub ++ https://github/com/cyclothymia/Socials-Email-Checker ]
""" + bcolors.ENDC)

filename = input("Enter the name of the file: ")

def twitter(line):
    email = line.strip()
    proxy = workingProxy()
    proxies = {
        "http": "http://" + proxy
    }
    r = requests.Session()
    url = "https://api.twitter.com/i/users/email_available.json?email=" + email
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    Host = "api.twitter.com"
    Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    r.headers = {'User-Agent': useragent}
    r.headers = {'Host': Host}
    r.headers = {'Accept': Accept}
    req = r.get(url, proxies=proxies).json()
    text = str(req)
    print(text)
    print('')
    if text.find("'valid': False") == True:
        file = open("twitter-linked.txt", "a")
        file.write(email + "\n")
        file.close()
        print(bcolors.OKGREEN + f"{email} = is linked to an account" + "\n" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + f"{email} = is not linked to an account" + "\n" + bcolors.ENDC)


if __name__ == "__main__":
    freeze_support()
    emails = open(f"{filename}")
    lines = emails.readlines()
    pool = Pool(processes=100)
    pool.map(twitter, lines)