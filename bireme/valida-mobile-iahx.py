# Descricao do script
# baixar os arquivos config.xml das instancias de iahx
# exemplo http://pesquisa.bvsalud.org/homeopatia/config/config.xml
# checar nesses arquivos o marcador <mobile_version>true</mobile_version>
# Listar os arquivos config.xml que nao tem esse marcador true



# doc = http://stackoverflow.com/questions/3893885/cheap-way-to-search-a-large-text-file-for-a-string
# doc = http://www.carlissongaldino.com.br/post/como-baixar-um-arquivo-com-python
# no site acima te da varias possibilidade de baixar - vou utilizar a urllib2
import urllib2


instancias = ['homeopatia', 'brasil', 'saudepublica']

i = 0
while i < 3:

#  url = 'http://pesquisa.bvsalud.org/%s/config/config.xml' % i
        # url = urllib2.Request('http://pesquisa.bvsalud.org/%s/config/config.xml' % i)
        url = ('http://pesquisa.bvsalud.org/%s/config/config.xml' % instancias[i])
        print url
        i = i + 1
        print "baixando com urllib2"
        f = urllib2.urlopen(url)
        data = f.read()
        # with open("config.xml",  "wb") as code:
        nome = instancias[i]
	print nome
	with open("config.xml",  "wb") as code:
	  code.write(data)
