# odbchelper.py

def buildConnectionString(params):
	"""  doc string """
	""" constroi uma string de conexao a partir de um dicionario de parametros """
# retorna uma string
	return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == '__main__':
	
	myParams = {"server": "mpilgrin", "database": "master", "uid": "sa", "pwd": "secret"}
	print buildConnectionString(myParams)
