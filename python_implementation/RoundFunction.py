import binascii
from Utilities import *
"""Key-Scheduling
Master K = k0 || k1
k0 = k'0 || k'2 -> Used for Pre- and Post- whitening (XOR addition with the current state)
k1 = k1,1 || k1,2 || k1,3 || k1,4 || k1,5 || k1,6 || k1,7 || k1,8
k1 is used to generate the subkeys fr(k1) 
fr(k1 ) = k1,1 || gr(1)(k1,2) || k1,3 || gr(2)(k1,4) || k1,5 || gr(3)(k1,6) || k1,7 || gr(4)(k1,8 )
for 1<=r<=20
where
gr(1)(x) = (x + 193r) mod 256
gr(2)(x) = (x + 165r) mod 256
gr(3)(x) = (x + 81r) mod 256
gr(4)(x) = (x + 197r) mod 256
"""
def f(i, k1):
	return bytetoInt(b''.join(inttoByte(g(bytetoInt(k1[j]), i, j//2)) if j%2 else inttoByte(k1[j])
	for j in range(8)))

def g(x, i, j):
	coeff = {0:193, 1:165, 2:81, 3:197}
	return (x+i*coeff[j])%256


"""Round function operations"""	
# Application of S-Box to the current state
def s(state):
	State = 0
	for i in range(16):
		State |= Sbox[(state>>(i*4))&0xf]<<(i*4)
	return State

# Application of Inverse S-Box to the current state
def sinv(state,Sinv):
	Sbox = Sinv
	State = 0
	for i in range(16):
		State |= Sbox[(state>>(i*4))&0xf]<<(i*4)
	return State
	
# XOR operation
def xor(state, key):
	return state ^ key

# Application of Permutation layer (P matrix) to the current state
def p(state):
	State = 0
	for i in range(64):
		State |= ((state >> i)&0b1) << p_mat[i]
	return State
	
# Application of Inverse Permutation layer (P_inv matrix) to the current state
def pinv(state):
	p = p_inv
	State = 0
	for i in range(64):
		State |= ((state >> i)&0b1) << p[i]
	return State
	
# Application of L layer (L matrices) to the current state
def l(state):
	llist = [l3,l2,l1,l0]
	State = 0
	for i in range(4):
		State |= multiplication(llist[i], (state>>(i*16))&0xffff)<<(i*16)
	return State
	
# Application of Inverse L layer (L_inv matrices) to the current state (Used in decryption)
def linv(state):
	llist = [l3inv,l2inv,l1inv,l0inv]
	State = 0
	for i in range(4):
		State |= multiplication(llist[i], (state>>(i*16))&0xffff)<<(i*16)
	return State

