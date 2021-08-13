# -*- coding: utf-8 -*-
import sys
import os
import re,time
import requests as r
import wget
os.system('clear')
def bannar():
  print ('''\033[95m
    
 
  _____ ____   __     ______   ___  
 |  ___| __ )  \ \   / /  _ \ / _ \ 
 | |_  |  _ \   \ \ / /| | | | | | |
 |  _| | |_) |   \ V / | |_| | |_| |
 |_|   |____/     \_/  |____/ \___/ 
                                         
''')
  print ('''\033[94m
    
   _____           _     _               
  / ____|         | |   | |              
 | |  __ _ __ __ _| |__ | |__   ___ _ __ 
 | | |_ | '__/ _` | '_ \| '_ \ / _ \ '__|
 | |__| | | | (_| | |_) | |_) |  __/ |   
  \_____|_|  \__,_|_.__/|_.__/ \___|_|   
                                         
                                         \033[93m Version : R.7     
                                    
''')
  print ('\033[94m-'*50)
  print ('')
  print (' \033[96m Creator  : \033[95m RaRe BlAcK')
  print ('')
  print (' \033[96m Tool     : \033[95m FB Videos Grabber')
  print ('')
  print (' \033[96m Facebook : \033[95m https://www.facebook.com/rareblack35')
  print ('')
  print (' \033[96m Github   : \033[95m https://github.com/rareblack35/')
  print ('')
  print (' \033[96m Coded By : \033[95m Quantum Cyber Squad' )
  print ('')
  print ('\033[94m-'*50)
  print ('')
  print ('             \033[0;37;41m FB Videos Grabber \033[0m ' )
  print ('')
  print ('')
bannar()

filedir = os.path.join('file.mp4')
ERASE_LINE = '\x1b[2K'
hibabe=input("\033[92m [!] Paste Your FB Video Url : \033[93m ")

print ('')
print ('')
print( '\033[0;37;44m Options Menu  : \033[0m ' )
print ('')
print ('')
print ('\033[91m [\033[0m1\033[91m] \033[92m Download SD Format\033[90m')
print ("")
print ('\033[91m [\033[0m✓\033[91m] \033[92m Download HD Format\033[90m')
print ("")
print ("")
choice=input(str('\033[92m [!] Type Any Number : \033[93m '))
print ("")
print ("")
print ("\033[96m [✓] WOW Downloading Video Wait Dear..Its Depends On Your Network Speed.To Stop This Process CTRL + Z")
print ("\033[91m")
if choice=='1':
  try:
    LINK = hibabe
    html = r.get(LINK)
    sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
  except r.ConnectionError as e:
  
    print("OOPS!! Connection Error.")
    
  except r.Timeout as e:
    print("OOPS!! Timeout Error")
  except r.RequestException as e:
    print("OOPS!! General Error or Invalid URL")  
  except (KeyboardInterrupt,SystemExit):
    print("Ok ok, quitting")
    sys.exit(1)
  except TypeError:
    print("Video May Private or Hd version not avilable")  
  else:
    sd_url = sdvideo_url.replace('sd_src:"', '')
    print("\n")
    print("\033[92m [+]Normal Quality:\033[93m " + sd_url)
    print("[+] Video Started Downloading")
    wget.download(sd_url, filedir)
    sys.stdout.write(ERASE_LINE)
    print("\n")
    print("Video downloaded")
    os.system('termux-setup-storage')
    os.system('mv file.mp4 /sdcard')
    print ('File Save As file.mp4 in Your Sdcard.')
    print ('Cheack Your Sdcard')
    print ('ALLAH HAFIZ ')
if choice=='2':
  try:
    print ("\033[91m")
    LINK = hibabe

    html = r.get(LINK)
    hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
  except r.ConnectionError as e:
  
    print("OOPS!! Connection Error.")
  except r.RequestException as e:
    print("OOPS!! General Error or Invalid URL")  
  except (KeyboardInterrupt,SystemExit):
    print("Ok ok, quitting")
    sys.exit(1)
  except TypeError:
    print("Video is Private or Hd version not avilable")    
  except r.Timeout as e:
    print("OOPS! Bad Luck! Timeout Error")
  else:
    hd_url = hdvideo_url.replace('hd_src:"', '')
    print("\n")
    print("\033[92m [+]Normal Quality:\033[93m " + hd_url)
    print("[+] Video Started Downloading")
    wget.download(hd_url, filedir)
    sys.stdout.write(ERASE_LINE)
    print("\n")
    print("Video downloaded")
    os.system('termux-setup-storage')
    os.system('mv file.mp4 /sdcard')
    print ('File Save As file.mp4 in Your Sdcard.')
    print ('Cheack Your Sdcard')
    print ('Allah Hafiz ')
else:
  print ('\033[Allah Hafiz')
  print ('Tnks For Support ')
 
  
