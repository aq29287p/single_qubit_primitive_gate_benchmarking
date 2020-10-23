import numpy as np
import scipy as sp
import scipy.linalg as la
import math
import cmath


def Id(n):
    return np.eye(n)

def pulse_op(a,noise):
	u = Id(2)
	for i in np.arange(0,len(a)):
		u = np.dot(op(a[i],0),u)

	return u

def rx(angle):
	return la.expm(-1j*X*angle/2)

def ry(angle):
	return la.expm(-1j*Y*angle/2)

def op(n,noise):

	if(n==0):
		return Id(2)
	if(n==1):
		return rx(pi)
	if(n==2):
		return rx(pi/2)
	if(n==3):
		return rx(-pi/2)
	if(n==4):
		return ry(pi)
	if(n==5):
		return ry(pi/2)
	if(n==6):
		return ry(-pi/2)




if __name__ == '__main__':

	Zero = np.matrix('1.0; 0.0')
	One = np.matrix('0.0; 1.0')

	X = np.matrix('0 1; 1 0')
	Y = np.matrix('0 -1j; 1j 0')
	Z = np.matrix('1 0; 0 -1')

	pi = math.pi

	Omega = 285.7e3

	'''
	params = {}


	for s in np.arange(0,24):
		seq = []
		print("Clifford # %d" % (s+1))
		print("Pulse sequence")
		while(True):
			ele = input()
			if(ele==''):
				break

			seq.append(int(ele))

		params['C'+str(s+1)] = seq
	'''
	params = np.load('params.npy',allow_pickle=True).item()
	print(params)

	cliff = []

	for s in np.arange(0,len(params)):

		u = Id(2)
		a = params['C'+str(s)]
		u = pulse_op(a,0)
		cliff.append(u)
		print("Clifford # %d" %(s))
		print(u)

	#np.save('./params.npy',params)
	np.save('./cliff.npy',cliff)
			
