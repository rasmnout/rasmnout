import sys
sys.path.append('/rasmnout/sys/')

import message
import os
import view
from colorama import *


print(message.info(message=f"Starting HTTP Server - software {Fore.RED}Apache2{Fore.RESET}"))
os.system("sudo systemctl enable apache2")
os.system("sudo systemctl start apache2")
print(message.info(message=f"Starting HTTP Executer - software {Fore.RED}RasmnoutExecuter{Fore.RESET}"))
view.run()
