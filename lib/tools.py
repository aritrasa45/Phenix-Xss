



from os import _exit
from time import sleep , strftime 
import sys

sys.dont_write_bytecode= True


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
            
        


retry = 0
threads = None
main_container = {}






    


def break_threads():
    
    global threads
    
    try:
        if not threads is None and len(threads) > 0:
            for T in threads:
                T = str(T).split(" ")[-1].strip("><)(")
                print(f"breaking thread: {Y}{T}{E}")
                sleep(0.01)
     
            info = "[INFO] all threads broken!"
            colorizer(info.upper() , C)            
            threads = None
            

    except KeyboardInterrupt:
        print("[!] Forefully exitted before breaking threads")
        _exit(0)



def retry_again(error):    

    global retry
    
    colorizer(error , R)    
    if retry > 0:
        retry -= 1
        info = f"[WARNING]  ({retry}) Retries left | <Trying again>"
        colorizer(info.upper(), Y)
          
        
    elif retry <= 0:
        info = "[INFO] Script Exitted || Add more retry numbers\n"
        info += "use --retry to stop error exitting!!"
        colorizer(info , R)
        break_threads()
        _exit(0)                               



def open_file(file):
    try:
        with open(file , "r") as f:
            content = f.read().splitlines()
            if len(content) > 0:
                return content , True
            return False , False
            
    except FileNotFoundError:
        return False , False

    except PermissionDeniedError:
        return False , False                

    except KeyboardInterrupt:
        print("\nabort")
        break_threads()
        _exit(0)                             





def colorizer(inp, clr):
    
    text = inp.split(" ")    
    other = ' '.join(text[1:])
    T = strftime("%H:%M:%S") 
    
    meth = [
                "[WARNING]", 
                "[INFO]", 
                "[ERROR]",
                ]
    
    if text[0].upper() == meth[0]:
        
        text = f"[{C}{T}{E}] {BLD}{G}{meth[0]}"
        text += f"{E}{clr} {other}{E}"
        print(text)

    elif text[0].upper() == meth[1]:
        text = f"[{C}{T}{E}] {BLD}{Y}{meth[1]}"
        text += f"{E}{clr} {other}{E}"               
        print(text)     
    
    elif text[0].upper() == meth[2]:
        text = f"[{C}{T}{E}] {BLD}{G}{RB}{meth[2]}"
        text += f"{E}{clr} {other}{E}"
        print(text)
        



def check_args(args, type):

    if args and args.endswith(".txt"):
        
        filename = args
        all , error = open_file(filename)
        
        if all and error:
            info = f"[INFO] Found {type} from {filename} of len {len(proxies)}\n"      
            info += "using random {type} for attacking"
                        
            colorizer(info , G)                  
            return all
            

        else:
            info = f"[ERROR] error fetching {type} from {filename} <{type.upper()}>"             
            retry_again (info)
            return None
            
    elif args:
        info = f"[INFO] Using {args} as {type}"
        colorizer(info , G)
        return args    
        
                
def num_clor(tot_int:int , num:float) -> float:
    
    if tot_int <= 1 and tot_int <= 2:
        return f"{G}{num}{E}"
                 
    elif tot_int <= 3 and tot_int <= 5:
        return f"{Y}{num}{E}"                
                
    elif tot_int >= 6:
        return f"{R}{num}{E}"


def input_handler(info , default="Y"):
    
    retry_again(info)
    typo = "[y/N]"     
    
    if default == "Y":typo = "[Y/n]"                                
         
    try:
        text = "{}Do you wanna continue [Y/n] :{}".format(BLD , E)
        user_input = input(text)
        
        if user_input =="":
            if typo[1:2].isupper():
                return True
            return False

        elif user_input.lower() == "y":
            return True            
        return False
        
    except KeyboardInterrupt:
        print("\nabort")
        break_threads()
        _exit(0)                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                            