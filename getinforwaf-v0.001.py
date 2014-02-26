#! /usr/bin/python
import urllib
import sys
import dns.resolver #pip install dnspython

if len(sys.argv) == 2:
	try:
		host = sys.argv[1]
		u = urllib.urlopen('http://'+host)
		ip = dns.resolver.query(host, 'A')
		for i in ip:
			print "\n"
			print u.geturl()
			print i
			print "\n"
			print u.headers
			print "\n"
			''' Permite escoger los valores del header 
			print u.code
			print u.info()['server']
			print u.info()['x-powered-by']
			print u.info()['content-type'] '''
	except: 
		e = sys.exc_info()[0]
		print "Error al obtener informacion"

else:
	print "\n Modo de Uso: $python webinforwaf.py <www.example.com>"
	print len(sys.argv)
