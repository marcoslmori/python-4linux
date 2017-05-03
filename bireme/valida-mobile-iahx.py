# Descricao do script
# baixar os arquivos config.xml das instancias de iahx
# exemplo http://pesquisa.bvsalud.org/homeopatia/config/config.xml
# checar nesses arquivos o marcador <mobile_version>true</mobile_version>
# Listar os arquivos config.xml que nao tem esse marcador true

import urllib2

instancias = ['portal', 'homeopatia', 'brasil', 'saudepublica']

i = -1
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
        i = i + 1
