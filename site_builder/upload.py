#!/bin/env python
#-*- coding: utf-8 -*-

import ftplib
import os
import os.path
import sys

FTP_URL = 'ftp.robyp.x10host.com'
FTP_USER = r'webmaster@robyp.x10host.com'
FTP_PW = 'y24upuStahes'
LOCAL_DIR = '/home/robby/Dropbox/Code/python/pymotw-it2.0/html'
REMOTE_DIR = '.'

tot_sent = 0
def _byte_counter(line):
	global tot_sent
	tot_sent += len(line)

def upload(lista_file, local_dir=LOCAL_DIR, host=FTP_URL,
           user=FTP_USER, pw=FTP_PW, remote_dir='/'):
	global tot_sent
	if not lista_file:
		print "Nessun file da trasferire"
		return
	ftp = ftplib.FTP(host=host)
	ftp.login(user, pw)
	ftp.cwd(remote_dir)
	for f in [os.path.join(local_dir,f) for f in lista_file]:
		if not os.path.exists(f):
			print f, "non trovato"
		ext = os.path.splitext(f)[1]
		if ext.lower() in ('.html', '.css', '.txt'):
			tot_sent = 0
			print "Invio di %s ..." % (os.path.basename(f))
			fh = open(f)
			ftp.storlines("STOR " + os.path.basename(f), fh, _byte_counter)
			fh.close()
			print "\t--> inviati (%d bytes)\n" % (tot_sent)
	#ftp.close()
	ftp.quit()
		
if __name__ == '__main__':
	if len(sys.argv) > 1:
		to_upload = sys.argv[1:]
		try:
			upload(to_upload)
		except ftplib.Error as ftperr:
			print "Errore ftp:\n", ftperr
		except Exception as ex:
			print "Errore generico\n", ex