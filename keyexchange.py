#!/usr/bin/env python
"""
name: saurabh chopra
student number: 250993097
this program will read the student number i.e private key from STDIN and print the output
output i.e.  input params and client public key and shared secret 
"""
import hashlib
from binascii import hexlify 


class KeyExchange(object):

	def __init__(self, clientprivateKey):
		"""
		Generate the public and private keys.
		"""		
		default_keyLength = 540
		# given in the question
		default_generator = 2		
		self.generator = default_generator
		self.keyLength = default_keyLength
		# given in the question
		self.prime = 179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007
		self.privateKey = clientprivateKey
		self.publicKey = self.genPublicKey()

	def genPublicKey(self):
		"""
		Generate a public key X with g**x % p.
		"""
		return pow(self.generator, self.privateKey, self.prime)

	def checkPublicKey(self, otherKey):
		"""
		Check the other party's public key to make sure it's valid.
		Since a safe prime is used, verify that the Legendre symbol == 1
		"""
		if(otherKey > 2 and otherKey < self.prime - 1):
			if(pow(otherKey, (self.prime - 1)//2, self.prime) == 1):
				return True
		return False

	def genSecret(self, privateKey, otherKey):
		"""
		Check to make sure the public key is valid, then combine it with the
		private key to generate a shared secret.
		"""
		if(self.checkPublicKey(otherKey) == True):
			sharedSecret = pow(otherKey, privateKey, self.prime)
			return sharedSecret
		else:
			raise Exception("Invalid public key.")

	def genKey(self, otherKey):
		"""
		Derive the shared secret, then hash it to obtain the shared key.
		"""
		self.sharedSecret = self.genSecret(self.privateKey, otherKey)

		# Convert the shared secret (int) to an array of bytes in network order
		# Otherwise hashlib can't hash it.
		try:
			_sharedSecretBytes = self.sharedSecret.to_bytes(
				self.sharedSecret.bit_length() // 8 + 1, byteorder="big")
		except AttributeError:
			_sharedSecretBytes = str(self.sharedSecret)

		s = hashlib.sha256()
		s.update(bytes(_sharedSecretBytes))
		self.key = s.digest()

	def showParams(self):
		print("Parameters:")
		print("Prime[{0}]: {1}".format(self.prime.bit_length(), self.prime))
		print("Generator[{0}]: {1}\n".format(self.generator.bit_length(),
			self.generator))
		print("Private key[{0}]: {1}\n".format(self.privateKey.bit_length(),
			self.privateKey))
		print("Public key[{0}]: {1}".format(self.publicKey.bit_length(),
			self.publicKey))

	def showResults(self):
		print("Results:")
		print("Shared secret[{0}]: {1}".format(self.sharedSecret.bit_length(),
			self.sharedSecret))
		print("Shared key[{0}]: {1}".format(len(self.key), hexlify(self.key)))

if __name__=="__main__":
	"""
	pass the client private key through STDIN	
	"""
	clientprivateKey = int(raw_input("enter student number: "))
	client = KeyExchange(clientprivateKey)
	#server public key is given in the question
	# g**y
	serverPublicKey = 139022310633144848563227990522588962361491877869038855065829826514882703858573603298090413311431369431081524652984000846147358384613784808314647138088643355402858109222089062652287044001960636786825183560316927615284929372700747820134313320367785847643272358844807908882152635681043748234327931229330129578283	
	client.genKey(serverPublicKey)
	client.showParams()
	client.showResults()
	raw_input("press any key to exit")
