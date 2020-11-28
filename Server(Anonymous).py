from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from msvcrt import getch
from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askdirectory
import random
import string
import socket
import os
from time import sleep
import sys


os.system("COLOR A")
os.system("CLS")


root = Tk()
root.withdraw()

Banner = r'''

  █████▒▄▄▄█████▓ ██▓███       ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███
▓██   ▒ ▓  ██▒ ▓▒▓██░  ██▒   ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒████ ░ ▒ ▓██░ ▒░▓██░ ██▓▒   ░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█▒  ░ ░ ▓██▓ ░ ▒██▄█▓▒ ▒     ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
░▒█░      ▒██▒ ░ ▒██▒ ░  ░   ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ▒ ░      ▒ ░░   ▒▓▒░ ░  ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░          ░    ░▒ ░        ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░
 ░ ░      ░      ░░          ░  ░  ░     ░     ░░   ░      ░░     ░     ░░   ░
                                   ░     ░  ░   ░           ░     ░  ░   ░
                               [ANONYMOUSE MODE]  [Github.com/Danushka-Madushan]

'''
print(Banner)


Authorizer = DummyAuthorizer()
USERNAME = socket.gethostname()
HOST_IP = socket.gethostbyname(USERNAME)
if HOST_IP == "127.0.0.1":
    print(">> Please Connect to Network Before Start FTP...")
    sleep(2)
    sys.exit()
PORT = 8000
HOST = (HOST_IP, PORT)


print(">> Starting FTP...")
sleep(1)

HOME = askdirectory(title='Selct Hosting Folder...')
if HOME == "":
    print(">> FTP Server Terminating...(No Folder Choosed!)")
    sleep(3)
    sys.exit()
Authorizer.add_anonymous(HOME, perm="elr")

print(
    f">> Server Address             : ftp://{HOST_IP}:{PORT}")
print("                              $ For Download and Upload Data Use Windows Explorer")
print(f">> Server Hosted Location     : [ {HOME} ]")
print("\n>> Server Started...")
Handler = FTPHandler
Handler.authorizer = Authorizer
Server = FTPServer(HOST, Handler)
Server.serve_forever()

root.mainloop()
