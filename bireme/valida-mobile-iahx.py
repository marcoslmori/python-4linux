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
# rm ./-config.xml


os.system("rm cfg/instancias.txt")
# os.system("echo '' > cfg/`instancias.txt")
os.system("ls -l bvsalud-org/pesquisa/htdocs/ |grep '^d' |awk '{ print $9 }' >> cfg/instancias.txt")
instancias = open('cfg/instancias.txt').read().splitlines()

i = 2
for (i,item) in enumerate(instancias):
       	url = ('http://pesquisa.bvsalud.org/%s/config/config.xml' % instancias[i])
	#print  url
	#print "=====for=======" + str(1)
	while True:
		try:
			f = urllib2.urlopen(url)
			data = f.read()
        		nome = ('xml/%s-config.xml' % instancias[i])
			with open(nome,  "wb") as code:
                            	code.write(data)
        		tree = ET.parse(nome)
        		root = tree.getroot()
        		for mobile_version in root.iter('mobile_version'):
               			 if mobile_version.text == "true":
                        		print nome +" mobile OK"
                                 else:
                                        print nome +" Mobile NOK"

			for show_related_docs in root.iter('show_related_docs'):
                                 if show_related_docs.text == "false":
                                        print nome +" Doc Relacionados  OK"
                                 else:
                                        print nome +" Doc Relacionados  NOK"

			i = i + 1
			print "------------------------------"
			break
		except Exception:
			# print "excecao - " + url
			i = i + 1
			break
#referencias
#https://docs.python.org/2/library/xml.etree.elementtree.html	
