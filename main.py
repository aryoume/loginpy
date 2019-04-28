import requests
import os
import json
import time
import collections 

datalog = '''
{
    "test01":{"user":"test01","pas":"test001"},"admin":{"user":"admin","pas":"adminsss"}
}
'''

title = '''
██╗      ██████╗  ██████╗ ██╗███╗   ██╗    ████████╗███████╗███████╗████████╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║       ██║   █████╗  ███████╗   ██║   
██║     ██║   ██║██║   ██║██║██║╚██╗██║       ██║   ██╔══╝  ╚════██║   ██║   
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║       ██║   ███████╗███████║   ██║   
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝       ╚═╝   ╚══════╝╚══════╝   ╚═╝
Test Login System By SL142 - https://facebook.com/iboy.sloth.1
(Ctrl + c to exit)
'''

thx = '''
████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗███████╗   
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝██╔════╝   
   ██║   ███████║███████║██╔██╗ ██║█████╔╝ ███████╗   
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗ ╚════██║   
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████║██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝
Thank for Use my Script. - SL142
'''

black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m" 
white="\033[0;37m"

logi = collections.defaultdict(lambda : 'Key Not found')

def main():
    os.system("clear")
    print(green + title)
    usrpass()
def usrpass():
    username = input("Username: ")
    password = input("Password: ")
    check(username,password)
def check(u,p):
    logi = json.loads(datalog)
    try:
        if p == logi[u]['pas']:
            print('[INFO] Success login....')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(0.5)
            os.system("clear")
            print(thx)
            time.sleep(1)
        else:
            print(red + '[ERROR] Password Wrong!' + green)
            time.sleep(1)
            main()
    except(KeyError):
        print(red + "[ERROR] Username Wrong!" + green)
        time.sleep(1)
        main()
try:
    main()
except(KeyboardInterrupt):
    os.system("clear")
    print(red + thx)
    print(red + "[OKAY] Exit Progarm")
    time.sleep(0.5)
    os.system("clear")
    print(red + thx)
    print(red + "[OKAY] Exit Progarm.")
    time.sleep(0.5)
    os.system("clear")
    print(red + thx)
    print(red + "[OKAY] Exit Progarm..")
    time.sleep(0.5)
    os.system("clear")
    print(red + thx)
    print(red + "[OKAY] Exit Progarm...")
    time.sleep(0.5)
    os.system("clear")
    print(red + thx)
    print(red + "[OKAY] Exit Progarm....")
    time.sleep(0.5)