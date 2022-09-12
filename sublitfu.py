from pyautogui import write
import time
from colorama import Fore,init

init(convert=True)
print(Fore.RED+"""
   _____       __    ___ __     ________  __
  / ___/__  __/ /_  / (_) /_   / ____/ / / /
  \__ \/ / / / __ \/ / / __/  / /_  / / / / 
 ___/ / /_/ / /_/ / / / /_   / __/ / /_/ /  
/____/\__,_/_.___/_/_/\__/  /_/    \____/   


""")							
                                                                  
print(Fore.GREEN+"""
  You don't have to sit and type stuff in Sublit anymore!!!
  Just copy and paste your code into sublit.txt file
  and run sublitfu.exe.
  Press y when you are ready, you will have 5 seconds 
  to switch to the sublit window.
  Once you switch click on the space where you type your code
  Thats it!!!
**Dont forget to delete the extra flower brackets at the end of your program**
""")



a=open("sublit.txt","r")

data=a.readlines()
while True:
        
    inp=input("Are you ready??y/n: ")
    if inp=="y":
        time.sleep(5)
        for i in data:
            
            write(i.strip()+"\n")
        hotkey('ctrl', 'shift', 'end')
        hotkey("delete")
    elif inp=="n":
        break
    else:
        print("Invalid option")

