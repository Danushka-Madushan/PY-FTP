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
                           [PROTECTED MODE]       [Github.com/Danushka-Madushan]

'''
print(Banner)

Authorizer = DummyAuthorizer()
USERNAME = socket.gethostname()
HOST_IP = socket.gethostbyname(USERNAME)
if HOST_IP == "127.0.0.1":
    print(">> Please Connect to Network Before Start FTP...")
    sleep(2)
    sys.exit()
else:
    pass
PORT = 8000
HOST = (HOST_IP, PORT)


letters_and_digits = string.ascii_letters + string.digits
result_str = ''.join((random.choice(letters_and_digits) for i in range(8)))

PASSKEY = result_str


print(">> Starting FTP...")
sleep(1)

HOME = askdirectory(title='Selct Hosting Folder...')

if HOME == "":
    print(">> FTP Server Terminating...(No Folder Choosed!)")
    sleep(3)
    sys.exit()
Authorizer.add_user(USERNAME, PASSKEY, HOME, perm="elradfmw",
                    msg_login=f"Successfully Logged in to {USERNAME}", msg_quit="Have a Nice Day...")


print(f">> LOGIN INFORMATION : USERNAME   : {USERNAME}")
print(f">> LOGIN INFORMATION : PASSWORD   : {PASSKEY}")
print(f">> SERVER HOSTED LOCATION         : [ {HOME} ]")
print(f">> FTP SERVER ADDRESS             : ftp://{HOST_IP}:{PORT}")


print("\n>> Server Started...\n\n")
Handler = FTPHandler
Handler.authorizer = Authorizer
Server = FTPServer(HOST, Handler)
Server.serve_forever()

root.mainloop()
