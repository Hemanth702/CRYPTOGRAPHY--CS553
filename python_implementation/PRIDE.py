import binascii
from binascii import unhexlify,hexlify
from Utilities import *
from RoundFunction import *
"""PRIDE Cipher implementation
	This class contains functions for implementation of 
	a)Encryption b)Decryption"""
	
"""
Encryption:
Step1: Application of P_inverse layer
Step2: Pre-whitening with k0

The below steps from 3-7 iterates for 19 times:
Step3: Application of P_inverse layer
Step4: Application of S-Box
Step5: Permutation layer (P layer)
Step6: Application of L matrices
Step7: Inverse permutation layer (P_inverse layer)

Step8: Post-whitening with k0
Step9: Application of P layer


Decryption:
Reverse of Encryption with Inverses replaced everywhere.
"""

class PRIDE(object):
	def __init__(self, key, noofrounds = 20):
		if len(key) != 16:
			raise ValueError("Key must be 16 bytes (128-bits)")
		self.k0,k1 = bytetoInt(key[:8]), key[8:]
		self.noofrounds = noofrounds
		self.roundKeys = [f(i+1,k1) for i in range(noofrounds)]
		
	def encryption(self, block):
		state = bytetoInt(block)
		# print(str(hexlify(inttoByte(state, 8))))
		state = pinv(state) 
		# print(str(hexlify(inttoByte(state, 8))))
		state = xor(state, self.k0) 
		# print(str(hexlify(inttoByte(state, 8))))
		for i in range(self.noofrounds):
			state = xor(state,pinv(self.roundKeys[i]))
			# print("pinv "+str(hexlify(inttoByte(pinv(self.roundKeys[i]),8))))
			# str(hexlify(inttoByte(state, 8)))
			# print("state: "+str(hexlify(inttoByte(state, 8))))
			state = s(state)
			# print("state: "+str(hexlify(inttoByte(state, 8))))
			if i!=self.noofrounds-1:
				state = p(state)
				# print("state: "+str(hexlify(inttoByte(state, 8))))
				state = l(state)
				# print("state: "+str(hexlify(inttoByte(state, 8))))
				state = pinv(state)
				# print("state: "+str(hexlify(inttoByte(state, 8))))
		state = xor(state, self.k0)
		# print("state: "+str(hexlify(inttoByte(state, 8))))
		state = p(state)
		# print("state: "+str(hexlify(inttoByte(state, 8))))
		return inttoByte(state, 8)
		
		
	def decryption(self, block):
		state = bytetoInt(block)
		state = pinv(state) 
		state = xor(state, self.k0)
		for i in range(self.noofrounds):
			state = sinv(state,Sinv)
			state = xor(state, pinv(self.roundKeys[-i-1]))
			if i!=self.noofrounds-1:
				state = p(state)
				state = linv(state)
				state = pinv(state)
		state = xor(state, self.k0)
		state = p(state)
		return inttoByte(state,8)
