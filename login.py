os.system('clear')
import sys
import time

def waktu(s):
 for c in s + '\n':
  sys.stdout.write(c)
  sys.stdout.flush()
  time.sleep(1./10)
waktu('\33[36;1mPilih No.1 untuk download pass dan ID nya')
time.sleep(3)
print "\x1b[32;1m[1] Unduh pass dan ID"
print "\33[32;1m[2] Masuk toolsnya"
pilih = raw_input('masukkan pilihan : ')
if pilih == '1':
      waktu('\33[32;1mokeh langsung saja kita download pass dan ID nya')
      waktu('\33[32;1msabar cok sedang membuka browser...')
      time.sleep(8)
      os.system('xdg-open https://safeku.com/3k09Vj')
if pilih == '2':
      waktu('\33[32;1mpastikan elu sudah tau pass dan ID nya sat')
      time.sleep(8)
      os.system('clear')
      time.sleep(3)

print '\x1b[1;33mSudah punya ID dan Password nya?'
print '\x1b[1;32mSilahkan Login '
import os, sys


def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


user = raw_input('ID: ')
import getpass
sandi = raw_input('Password: ')
if sandi == 'Cyber BSTRD' and user == 'MrBSTRD13':
    print 'Anda Telah Login'
    sys.exit
else:
    print 'Login GAGAL, Silahkan unduh pw dan ID nya'
    time.sleep(5)
    restart()