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
os.system("ls -l /pesquisa/htdocs/ |grep '^d' |awk '{ print $9 }' >> cfg/instancias.txt")
instancias = open('cfg/instancias.txt').read().splitlines()
id_google = []
id_google_dup = []
i = 1
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

                        print url                     

			for site in root.iter('site'):
                                        print site.text

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

			for google_analytics_tracking_id in root.iter('google_analytics_tracking_id'):
				print google_analytics_tracking_id.text
				if google_analytics_tracking_id.text in id_google:
				   id_google_dup.append(google_analytics_tracking_id.text)
       				else:
				   id_google.append(google_analytics_tracking_id.text)
				#print id_google


			i = i + 1
			print "------------------------------"
			break
		except Exception:
			# print "excecao - " + url
			i = i + 1
			break

#print id_google

print "ID de google analytics duplicados"

print  id_google_dup

print "------------------------------"

#referencias
#https://docs.python.org/2/library/xml.etree.elementtree.html	
