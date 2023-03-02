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

def instagram(line):
    email = line.strip()
    proxy = workingProxy()
    proxies = {
        "http": "http://" + proxy
    }
    r = requests.Session()
    url = "https://www.instagram.com/accounts/account_recovery_send_ajax"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    r.headers = {'User-Agent': useragent}
    r.headers.update({'X-CSRFToken': 'missing'})
    data = {"email_or_username": email}
    req = r.post(url, data=data, proxies=proxies)
    print(req.text)
    print('')
    if req.text.find("We sent an email to")>=0:
        file = open("instagram-linked.txt", "a")
        file.write(email + "\n")
        file.close()
        print(bcolors.OKGREEN + f"{email} = is linked to an account" + "\n" + bcolors.ENDC)
    elif req.text.find("password")>=0:
        file = open("instagram-linked.txt", "a")
        file.write(email + "\n")
        file.close()
        print(bcolors.OKGREEN + f"{email} = is linked to an account" + "\n" + bcolors.ENDC)
    elif req.text.find("sent")>=0:
        file = open("instagram-linked.txt", "a")
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
    pool.map(instagram, lines)