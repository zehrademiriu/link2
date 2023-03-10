import requests
import time
import os
from proxy import workingProxy
from requests.structures import CaseInsensitiveDict
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

def snapchat(line):
    email = line.strip()
    url = "https://bitmoji.api.snapchat.com/api/user/find"
    proxy = workingProxy()
    proxies = {
        "http": "http://" + proxy
    }
    r = requests.Session()
    Accept = "application/json"
    ContentType = "application/json"
    r.headers = {'Accept': Accept}
    r.headers = {'Content-Type': ContentType}
    req = r.post(url, headers=r.headers, json={"email":email}, proxies=proxies)
    status = req.status_code
    print(status)
    print('')
    if (status == 200):
        print(bcolors.OKGREEN + f"{email} = is linked to an account" + "\n" + bcolors.ENDC)
        file = open("snapchat-linked.txt", "a")
        file.write(email + "\n")
        file.close()
    else:
        print(bcolors.WARNING + f"{email} = is not linked to an account" + "\n" + bcolors.ENDC)

if __name__ == "__main__":
    freeze_support()
    emails = open(f"{filename}")
    lines = emails.readlines()
    pool = Pool(processes=100)
    pool.map(snapchat, lines)