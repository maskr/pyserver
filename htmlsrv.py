#David Crespo, 2017
class Web:
	def __init__(self, datos):
		self.frm = self.partir(datos)
		self.pttn = self.get_peticion()
		self.mtd = self.pttn[0]
		self.webfile = self.pttn[1]
		self.direccion = None
		self.tiene_extension = False
		self.cmds = self.get_comandos()
		self.get_direccion()
	def partir(self, datos):
		datos = datos.decode('utf-8')
		return datos.split('\r\n')
	def get_peticion(self):
		datos = self.frm[0]
		return datos.split(' ')
	def get_metodo(self):
		return self.mtd
	def not_found(self):
		self.direccion = 'sistema/404.html'
	def get_direccion(self):
		if self.webfile == '/':
			self.direccion = 'webs/index.html'
		else:
			try:
				ext = self.extension(self.webfile)
				if self.tiene_extension == False:
					self.direccion = self.get_directorio()+self.webfile+'.'+ext
				else:
					self.direccion = self.get_directorio()+self.webfile
				return self.direccion
			except:
				self.not_found()
				return self.direccion
	def get_directorio(self):
		ext = self.extension(self.webfile)
		sel_directorio = {
						'htm': 'webs', 
						'html': 'webs', 
						'css': 'css', 
						'ico': 'imgs', 
						'jpg': 'imgs', 
						'jpeg': 'imgs', 
						'pdf': 'docs', 
						'js': 'scripts', 
						'avi': 'media', 
						'mp3': 'media', 
						'zip': 'varios', 
						'ogg': 'media', 
						'ttf': 'fonts', 
						'mp4': 'media', 
						'mkv': 'media', 
						'png': 'imgs', 
						'rar': 'varios'}
		return sel_directorio.get(ext)
	def comandos(self):
		return self.cmds.split('&')
	def ordenes(self):
		lista = []
		com = []
		for i in self.comandos():
			com = i.split('=')
			lista += [com]
		return lista
	def get_comandos(self):
		a=0
		for i in self.frm:
			if i == '':
				#print(self.frm[a+1])
				return str(self.frm[a+1])
				break
			else:
				a = a + 1
	def metodo_post(self):
		print(self.ordenes())
	def es_texto(self):
		ext = self.extension(self.webfile)
		sel_contenido = {
						'htm': True, 
						'html': True, 
						'css': True, 
						'ico': False, 
						'jpg': False, 
						'jpeg': False, 
						'pdf': False, 
						'js': True, 
						'avi': False, 
						'mp3': False, 
						'zip': False, 
						'ogg': False, 
						'ttf': False, 
						'mp4': False, 
						'mkv': False, 
						'png': False, 
						'rar': False}
		return sel_contenido.get(ext)
	def tipos_mime(self):
		ext = self.extension(self.direccion)
		sel_tipo = {
					'htm': 'text/html', 
					'html': 'text/html', 
					'css': 'text/css', 
					'ico': 'image/x-icon', 
					'jpg': 'image/jpeg',
					'jpeg': 'image/jpeg', 
					'pdf': 'application/pdf', 
					'js': 'application/javascript', 
					'avi': 'video/avi', 
					'mp3': 'audio/mpeg3', 
					'zip': 'application/zip', 
					'ogg': 'application/ogg', 
					'ttf': 'application/x-font-ttf', 
					'mp4': 'video/mp4', 
					'mkv': 'video/x-matroska', 
					'png': 'image/png', 
					'rar': 'application/x-rar-compressed'}
		return sel_tipo.get(ext)
	def extension(self, nombre):
		try:
			ext = nombre.split('.')
			self.tiene_extension = True
			return ext[1]
		except:
			self.tiene_extension = False
			return 'html'
	def web_head(self):
		return 'HTTP/1.1 200 OK\r\nContent-Type: %s\r\n\r\n'%(self.tipos_mime())
