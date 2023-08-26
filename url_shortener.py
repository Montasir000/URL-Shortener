#FOLLOW MY GITHUB : https://github.com/Montasir000
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
cyan="\033[0;36m"         # Cyan

import os
try:
    import pyshorteners
except ModuleNotFoundError:
    os.system('pip install pyshorteners > /dev/null')
url=input(cyan+' ENTER YOUR LONG URL : ')
shortx=pyshorteners.Shortener()
short_url=shortx.tinyurl.short(url)
print(green+' YOUR SHORT URL IS : '+short_url)
print(yellow+'Thank you.')