class Address:
	address = "0.0.0.0"
	port = 8080
	def __init__(self, address, port):
		self.address = address
		self.port = port

	def getAddress(self):
		return self.address
	
	def getPort(self):
		return self.port