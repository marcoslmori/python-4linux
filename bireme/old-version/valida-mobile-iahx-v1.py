# Descricao do script
# baixar os arquivos config.xml das instancias de iahx
# exemplo http://pesquisa.bvsalud.org/homeopatia/config/config.xml
# checar nesses arquivos o marcador <mobile_version>true</mobile_version>
# Listar os arquivos config.xml que nao tem esse marcador true

import urllib2
import xml.etree.ElementTree as ET


instancias = ['portal', 'homeopatia', 'brasil', 'saudepublica']

# i = -1
# while i < 3:
for (i,item) in enumerate(instancias):
       	url = ('http://pesquisa.bvsalud.org/%s/config/config.xml' % instancias[i])
        # print url
	# print i, item
        f = urllib2.urlopen(url)
        data = f.read()
        nome = ('%s-config.xml' % instancias[i])
	# print nome
	with open(nome,  "wb") as code:
		code.write(data)
	#print nome
        #e = xml.etree.ElementTree.parse(nome).getroot()
	#print e
	tree = ET.parse(nome)
	root = tree.getroot()
	#print tree
	#print root
	#for neighbor in root.iter('mobile_version'):
	#	print neighbor.attrib
	#	print '---------------------------------'
	#for child in root:
	#	#print child.tag, child.attrib
	#	print child.tag	
	# print '---------------------------------'
	for mobile_version in root.findall('mobile_version'):
		rank = mobile_version.find('true').txt
		name = mobile_version.get('true')
	print name, rank

	i = i + 1
#https://docs.python.org/2/library/xml.etree.elementtree.html
	
