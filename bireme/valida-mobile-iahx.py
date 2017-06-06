#!/usr/bin/python
# Descricao do script
# baixar os arquivos config.xml das instancias de iahx
# exemplo http://pesquisa.bvsalud.org/homeopatia/config/config.xml
# checar nesses arquivos o marcador <mobile_version>true</mobile_version>
# Listar os arquivos config.xml que nao tem esse marcador true

import urllib2
import xml.etree.ElementTree as ET
import os
import commands
#  rm ./-config.xml


os.system("echo '' > instancias.txt")
os.system("ls -l /xxxxxxx/pesquisa/htdocs/ |grep '^d' |awk '{ print $9 }' >> cfg/instancias.txt")
instancias = open('cfg/instancias.txt').read().splitlines()

i = 1
for (i,item) in enumerate(instancias):
       	url = ('http://pesquisa.bvsalud.org/%s/config/config.xml' % instancias[i])
	#print "=====for=======" + str(1)
	while True:
		try:
			f = urllib2.urlopen(url)
	 		#print "=====try=======" + str(1) 
			data = f.read()
        		nome = ('xml/%s-config.xml' % instancias[i])
			#print nome 
                        with open(nome,  "wb") as code:
                            code.write(data)
        		tree = ET.parse(nome)
        		root = tree.getroot()
        		for mobile_version in root.iter('mobile_version'):
               			 if mobile_version.text == "true":
                        		print nome +" ok"
			break
		except Exception:
			print "=====except=======" + str(i)
			print nome + " url invalida"
		 	break
			#pass
	#with open(nome,  "wb") as code:
	#	code.write(data)
	#tree = ET.parse(nome)
	#root = tree.getroot()
	#for mobile_version in root.iter('mobile_version'):
	#	if mobile_version.text == "true":
	#		print nome +" ok"	
	#print "=====fim=======" + str(1)
	i = i + 1
	print str(i)
#referencias
#https://docs.python.org/2/library/xml.etree.elementtree.html
	
