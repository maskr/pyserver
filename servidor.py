#GNU/GPL David Crespo, 2017
import socket
import htmlsrv
DIRECCION = '0.0.0.0'
PUERTO = 80
BUFFER = 1024
def abrir(fichero):
	fichero = open(fichero, 'r')
	web = fichero.read()
	fichero.close()
	return web
def rsp(conn):
	peticion = htmlsrv.Web(conn.recv(BUFFER))
	if peticion.get_metodo()=='POST':
		ord = peticion.ordenes()
		print(ord)
	if peticion.es_texto():
		cadena = peticion.web_head()
		try:
			enviar = abrir(peticion.direccion)
		except:
			peticion.not_found()
			cadena = peticion.web_head()
			enviar = abrir(peticion.direccion)
		enviar = bytes(cadena+enviar, 'utf-8')
		conn.send(enviar)
	else:
		cadena = bytes(peticion.web_head(), 'utf-8')
		try:
			with open(peticion.direccion, mode='rb') as fichero:
				conn.send(cadena)
				conn.sendfile(fichero)
				fichero.close()
		except:
			peticion.not_found()
			cadena = peticion.web_head()
			enviar = abrir(peticion.direccion)
			enviar = bytes(cadena+enviar, 'utf-8')
			conn.send(enviar)
	conn.close()
def Main():
	srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srvr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	srvr.bind((DIRECCION, PUERTO))
	srvr.listen(4)
	while 1:
		(conexion, (origen, puerto)) = srvr.accept()
		rsp(conexion)
Main()
	
