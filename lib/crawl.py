

from os import chdir , _exit
import requests 
from bs4 import BeautifulSoup 
import sys


sys.dont_write_bytecode= True

from lib.tools import *

BLD = '\033[1m' #BOLD

R = BLD + '\033[31m' # RED
G = '\033[32m' # GREEN 
Y = '\033[33m' # YELLOW
B = '\033[34m' # BLUE
C = '\033[36m' # CYAN
M = '\033[35m' # MAGENTA
    
E = '\033[0m'
    
MB = '\033[45m' # background magenta
YB = '\033[43m' # yellow background 
GB = '\033[42m' # green background
RB = '\033[41m' #red background
        



def start_crawl(domain, do_crawl):
    
    links_all = []    
    html= None
    
    if not do_crawl:return domain
    
    try:
    
        response = requests.get(domain)
        html = response.text
        status = response.status_code
        
        info = f"[INFO] Sent a get request to {domain} to crawl "
        colorizer(info , G)
        
    except requests.RequestException:
        info = "[ERROR] An error occured when sending request"
        
        if input_handler(info , default="N"):
            try:
                try:
                    pass
                except:
                    pass
            except:
                pass
                pass
                                        
                    
                    
        else:
            info = "[INFO] Stopped crawling"
            colorizer(info , R)        
            return domain 
               
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                 
    
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    all_urls = 0    
  
    
    for count , link in enumerate(links):
        href = link.get('href')
        if href and domain not in href and (href.startswith('http://') or href.startswith('https://')):           
            
      
            try:
                res = requests.get(href)
            
                if res.status_code == 200:
                                
                    links_all.append(href)
                    print("{}{}{}{}".format(BLD , Y , href , E))                           
                    all_urls += 1
                
                    info = f"[INFO] Found valid crawl url(s) {count + 1}/{all_urls}"
                    colorizer(info , G)

                else:all_urls += 1
                
            except KeyboardInterrupt:
                print("\nabort")
                break_threads()
                _exit(0)       
                                                
            except requests.RequestException:
                all_urls += 1
        
                                                                            
    links_all = list(set(links_all))  
    return links_all
  
