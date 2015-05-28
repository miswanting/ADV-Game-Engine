#coding=utf-8
#本文件提供了以下对象：
import socket

class TCPServer:
	def __init__(self):
		srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		srvsock.bind(('', 9527))
		srvsock.listen(5)
		while True:
			clisock, (remoteHost, remotePort) = srvsock.accept()
			print "[%s:%s] connected" % (remoteHost, remotePort)
			#do something on the clisock
			clisock.close()
	def send(self, text):
		pass
	def recv(self):
		pass
class TCPClient:
	def __init__(self):
		clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clisock.connect(('localhost', 9527))
		#I/O on this clisock
		#clisock.send("")
		#dat = clisock.recv(len)
		print dat  
	def send(self, text):
		pass
	def recv(self):
		pass
class UDPServer:
	def __init__(self):
		address = ('', 9527)
		srvsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		srvsock.bind(address)
		#data,addr = srvsock.recvfrom(2048)
	def send(self, text):
		pass
	def recv(self):
		pass
class UDPClient:
	def __init__(self):
		address = ('localhost', 9527)
		clisock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#clisock.sendto(data, address)
	def send(self, text):
		pass
	def recv(self):
		pass
class netServer:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def __init__(self):
		pass
	def startServer(self, host = '', port = 50007):
		self.s.bind((host, port))
		self.s.listen(1)
		self.conn, addr = self.s.accept()
		print('Connected by', addr)
		while True:
			if not self.recv(): break
			self.send(self.recv())
	def send(self, data):
		self.conn.sendall(data)
	def recv(self):
		return conn.recv(1024)
	def close(self):
		self.conn.close()
class netClient:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def __init__(self):
		pass
	def connectServer(self, host, port):
		self.s.connect((host, port))
		self.send()
		print(self.recv())
	def send(self, data = b'Hello, world'):
		self.s.sendall(data)
	def recv(self, timeOut = 1024):
		data = self.s.recv(timeOut)
		return(repr(data))
	def close(self):
		self.s.close()
if __name__ == '__main__':
	#实例化
	I = mapCloud()
	