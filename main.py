#Xss_script | MAIN


try:
    import requests as Req
    from requests.exceptions import *
    from random import choice , randint
    from time import sleep , time
    from threading import Thread
    from os import _exit 
    import os
    from socket import inet_aton 
    from socket import error as SockErr
    from base64 import b64encode 
    import argparse
    import sys
    
    
    from lib.tools import check_args
    from lib.tools import colorizer 
    from lib.tools import retry_again
    from lib.tools import break_threads 
    from lib.tools import num_clor
    from lib.tools import input_handler     
    
    from lib.crawl import start_crawl
    
    import lib.tools as global_variable

except KeyboardInterrupt:
    print("\nuser aborted")
    raise SystemExit 
        
    
sys.dont_write_bytecode= True


R = '\033[31m' # RED
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
        
BLD = '\033[1m' #BOLD




def logo():
    print(BLD , Y)
    print(r"""
    ___         _ __                           
   /   |  _____(_) /__________ __________ _    
  / /| | / ___/ / __/ ___/ __ `/ ___/ __ `/    
 / ___ |/ /  / / /_/ /  / /_/ (__  ) /_/ /     
/_/  |_/_/  /_/\__/_/   \__,_/____/\__,_/""")
    print(choice([R , G , Y , B , M]))
    print("~A powerful XSS Tool made by aritrasa45~")
    print(E)
    
    

        

        
def check_netwk():
    
    total = 0            
    info = "[INFO] checking the netwk before proceeding!"
    colorizer(info , Y)
    
    urls = [
            "https://google.com",
            ]

    for i in range(3):
        try:
            s_time = time()            
            Req.get(urls[0])
            
            total += int(round((time() - s_time), 2))
            info = f"[INFO] checking connection before staring {i + 1}/3 | {total}s"
            colorizer(info , G)


        except KeyboardInterrupt:
            print("\nabort")
            _exit(0)
                        
        except Exception as e:
            total += 0
            info = "[ERROR] An error happend when sending ping!!"
            colorizer(info , R)                       


    if total >= 60 or total <= 0:
        print(f"{R}bad netwk! Please check your connection!!{E}")
        _exit(0)

                                                

def without_schema():
    if "https://" in url[0:8]:
        return [url[8:] , "https"]   
    return [url[7:], "http"]
    
            
    
def check_protocol():
  
    global url  
  
    url = url.strip()
    info = f"[INFO] Checking url schema protocol"
    colorizer(info , BLD +Y)
    
    if not "https://" in url[0:8] or "http://" in url[0:7]:
        try:
            Req.head(''.join(["https://", url]))
            url = ''.join(["https://", url])            
            info = f"[INFO] added https schema -> {url}"
            colorizer(info , G)
            return
             
        except:pass
        
        try:
            Req.head(''.join(["http://", url]))
            url = ''.join(["http://", url])
            info = f"[INFO] added http schema  -> {url}"
            colorizer(info , G)            
            return
                                                          
        except Exception:
            info = f"[ERROR] An error occured when fetching schema!"
            colorizer(info , R)
            _exit(0)
    
    info = f"[INFO] Detected schema {url} -> {without_schema()[1]}"
    colorizer(info , BLD + Y)    







        
              


def start_Xss():
    
    global count
    

    while count != 0:
        
        try:
            
            agents = choice(user_agent) if user_agent else None            
            url_ = choice(url) if isinstance(url, list) else url
                                    
            
            proxies_all = str(proxy)        
            if isinstance(proxy , list):
                proxies_all = choice(proxy)


            payload_key = str(payload)                             
            if isinstance(payload, list):
                payload_key = choice(payload)


            payload_value = str(Xss).encode()            
            if isinstance(Xss , list):
                payload_value = choice(Xss).encode()

        
            header = {
                "User-Agent":agents or "Phenix|Xss 45" ,
                "Content-Type":"application/json" ,           
                "Accept-Encoding":"gzip , deflate" ,   
                "Accept": "*/*",  
                "Connection":"close",
            }       
             
            payload_all = {payload_key:payload_value.decode()}          
            
            proxies = {
                    "http": ''.join(["http://", proxies_all]) if proxy else None ,
                    "https": ''.join(["https://", proxies_all]) if proxy else None,
           }
            
            
            start_time = time()
            
            response = getattr(Req , method)(url_ ,          
            
            timeout=timeout or None ,             
            proxies = proxies or None ,  
                        
            headers=header ,
            params= payload_all ,
            )
                                                  
            
            total = round(time() - start_time , 3)            
            status = response.status_code                      
            total = num_clor(int(total), total)
                        

                       
            
            if status != 200:
                status = f"{R}{status}{E}"
                info = "[WARNING] Server may not be accepting the connection"   
                colorizer(info , ''.join([BLD , R]))             
            else:status = f"{C}{status}{E}"           
            
                
            print(payload_all)
            info = f"[INFO] Sent {payload_all} to {url_} with "
            info += f"status code {status}"
            colorizer(info, Y)
            
                
            for keys , values in proxies.items():
                print(f"[PROXY] {keys} -> {G}{BLD}{values}{E}")
                

        
        except ReadTimeout:
            info = f"[INFO] ({method.upper()}) timeout exceeded! timeout ({timeout})"
            retry_again(info)
            
        except InvalidURL:
            host = without_schema()[0]
            info = f"[ERROR] Invalid URL {host}"
            retry_again(info)

        except HTTPError:
            info = "[ERROR] HTTP Error occurred!"
            retry_again(info)
            
        except (MissingSchema, InvalidSchema) as sch:
            if isinstance(sch , InvalidSchema):
                info = "[WARNING] Invalid schema given to url!!"
                retry_again(info)
                break_threads()
                _exit(0)
                
            else:
                info = f"[ERROR] Schema is missing! Trying to add schema"
                retry_again(info)           
                check_protocol()
      
            
        except ConnectionError:
            info = f"[ERROR] connection Errror [{url}]"
            retry_again(info)
            
        except TooManyRedirects:
            info = "[ERROR] Web server sending too many redirects! "
            
            if not input_handler(info, default="Y"):
                print("\nabort")
                break_threads()
                _exit(0)
                    
        
            
        except ChunkedEncodingError:
            info = "[ERROR] Connection broken , expected chunks to recive!!"
            retry_again(info)

        except KeyboardInterrupt:
            print( "\nabort!") 
            break_threads()
            _exit(0)                                                                                               
                                                
        finally:
            try:
                count -= 1
                sleep(sleep_)
            except KeyboardInterrupt:
                print("\nabort")
                break_threads()
                _exit(0)            


def main():
    
    global url 
    global count
    global timeout
    global sleep_
    global user_agent
    global Xss
    global method
    global proxy
    global payload

  
    logo()   
    
            
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter ,
    description='Phenix|XSS how to use ->'
    )
    
    parser.add_argument('url', help='The URL to scan')

    parser.add_argument('--count', type=int, default = 1000 ,
    help="number of count loop to exit when matches")
    
    parser.add_argument( '--retry', type=int, default = 0 ,
    help="number of retry to do in any errors")    
    
    
   
    parser.add_argument( '--timeout', type=int , default = None , 
    help="the timeout of the request until it fails")      
    
    parser.add_argument( '--user_agent', type=str ,default = None , 
    help="the user agent to send with")
    
    
    
    parser.add_argument( '--sleep', type=int ,default = 2 , 
    help="the delay between each request")
    
    parser.add_argument( '--Xss', type=str ,default = None ,
    help="Xss headers , (use filename for opeining and reading file xss)")
    
    
    
    parser.add_argument( '--method', type=str ,default = "GET" , 
    help="request method [GET , POST , PUT , DELETE]")

    parser.add_argument( '--threads', type=int ,default = 0 , 
    help="multiple threads to run concurrently")
    

    parser.add_argument( '--proxy', type=str ,default = None , 
    help="use proxies when sending request")
    
    parser.add_argument( '--crawl', action= 'store_true' , 
    help="to enable url crawl")
    
    
    parser.add_argument( '--payload_key', type=str , default= None ,
    help="keys for sending query params with xss as values")
    
 
    args = parser.parse_args()      
    supported_meth = [
         "GET", "POST", "PUT",  "DELETE"
         ]
              
    sleep_ = args.sleep       
    url = args.url
    
    
    global_variable.threads = []
    global_variable.retry = args.retry
    

    proxy = check_args(args.proxy , "proxy")
    
    if not proxy is None:
        host_port = proxy.split(":")
        
        if isinstance(host_port , list):
                        
            info = "[INFO] Using 8080 as default port for proxy"
            colorizer(info , BLD + Y)
            
            proxy += ":8080"            
            host_port = proxy.split(":")
            
        try:
            inet_aton(host_port[0])
            proxy = ':'.join([host_port[0] , host_port[1]])
            info = f"[INFO] Using {proxy} as proxy "
            colorizer(info , G)
            
        except SockErr:
            info = "[ERROR] Error while indentifying proxy"  
            retry_again(info)        
            proxy = None
            
        except KeyboardInterrupt:
            print("\nabort")
            _exit(0)   
    
    
    Xss = check_args(args.Xss , "Xss")
    user_agent = check_args(args.user_agent, "user-agent")
    payload = check_args(args.payload_key , "payload_key")

                                                                                                                                                                                                                        
                                                                                                                   
            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            
    if args.method.upper() not in supported_meth:
        print(f"{G}supported methods -> {E}",supported_meth)   
        _exit(0)                                                            
                                                            
    if not args.timeout is None and args.timeout <= 0:
        print(f"{R}cannot use timeout les or equal to 0{E}")
        _exit(0)              
                                      

    check_netwk()  
    check_protocol() 
    url = start_crawl(url, args.crawl)  
      

    timeout = args.timeout
    count = args.count   
    method = args.method.lower()
    
    
                                    
    
    if args.threads > 0:
        cpu = os.cpu_count()
        if args.threads > cpu:
            info = f"{BLD}{R}[!] cpu(T) {cpu} Using {args.threads}{E}"
            print(info)
            
        for T in range(1 , args.threads + 1):
            print(f"{G}({T}){E} Thread processing to start Xss")
            T = Thread(target = start_Xss)
            T.start()
            global_variable.threads.append(T)

    
    args.proxy = "YES" if args.proxy else "NO"      
    args.user_agent = "YES" if args.user_agent else "NO" 
    args.Xss = "YES" if args.Xss else "NO"             
                                                                                                                                                                                        
    for key ,value in vars(args).items():
        if value and isinstance(value , str):
            value = value.upper()
        print(f"\t{key}: {BLD}{G}{value}{E}")
        
    start_Xss()

if __name__ == '__main__':
    try:
        main()        
    except KeyboardInterrupt:
        print("\nabort")
        break_threads()
        _exit(0)       