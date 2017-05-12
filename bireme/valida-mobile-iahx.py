# Descricao do script
# baixar os arquivos config.xml das instancias de iahx
# exemplo http://pesquisa.bvsalud.org/homeopatia/config/config.xml
# checar nesses arquivos o marcador <mobile_version>true</mobile_version>
# Listar os arquivos config.xml que nao tem esse marcador true

import urllib2
import xml.etree.ElementTree as ET
import os
import commands

# implementar via sistema operacioanl ls -l /home/apps/bvsalud-org/pesquisa/htdocs/ |grep "^d" |awk '{ print $9 }'
# instancias = ['portal', 'homeopatia', 'brasil', 'saudepublica']i
# para apagar esse arquivo.  tem que descobrir por que cria 
#  rm ./-config.xml

os.system("")
instancias = open('cfg/instancias.txt').read().splitlines()

# print instancias

#=arq = open('/tmp/lista.txt', 'w')


# i = -1
# while i < 3:
for (i,item) in enumerate(instancias):
       	url = ('http://pesquisa.bvsalud.org/%s/config/config.xml' % instancias[i])
        # print url
	# print i, item
	# f = urllib2.urlopen(url)
       	while True:
		try:
			f = urllib2.urlopen(url)
	 		data = f.read()
        		#print data
        		nome = ('%s-config.xml' % instancias[i])
			print nome
			# print nome
			break
		except Exception:
			print url
			print 'url invalida'
			break

	with open(nome,  "wb") as code:
		code.write(data)
	#print nome
        #e = xml.etree.ElementTree.parse(nome).getroot()
	#print e
	tree = ET.parse(nome)
	root = tree.getroot()
	#root = ET.fromstring(site_data_as_string)
	#print tree
	print '---------------------------------- '
	#print root
	# testar o findint interesting elements no link do final da pagina
	for mobile_version in root.iter('mobile_version'):
	#	print mobile_version.text
	#valida_mobile = mobile_version.txt	
		if mobile_version.text == "true":
			print nome +" ok"	
	i = i + 1
#referencias
#https://docs.python.org/2/library/xml.etree.elementtree.html
	
