import numpy as np
import scipy as sp
import scipy.linalg as la

import math
import cmath


X = np.matrix('0 1;1 0')
Y = np.matrix('0 -1j; 1j 0')
Z = np.matrix('1 0; 0 -1')
pi = math.pi

def Id(N):
    return np.eye(N) 



cliff = np.load('./cliff.npy')


def infid(A,B):
    A = np.matrix(A)
    B = np.matrix(B)
    F = np.dot(B.getH(),A)
    F = np.trace(F)
    F = 1-F**2/4
    return F

def cliff_inv(A):
	error = []
	for s in range(len(cliff)):
		U = np.dot(A,cliff[s])
		r = infid(U,Id(2))
		error.append(r)
	min_value = np.amin(error)
	
	for s in range(len(cliff)):
		r = error[s]
		if(r == min_value):
			N = s
	return N	


def cliff_num(A):
	error = []
	for s in range(len(cliff)):
		D = cliff[s]
		r = infid(A,D)
		error.append(r)
	min_value = np.amin(error)

	for s in range(len(error)):
		r = error[s]
		if(r == min_value):
			N = s
	return N

if __name__ == '__main__':

	cliff_list = []

	for s in np.arange(0,len(cliff)):
		for j in np.arange(0,len(cliff)):
			C = np.dot(cliff[s],cliff[j])
			n = cliff_num(C)
			cliff_list.append(n)    

	cliff_list = np.array(cliff_list)
	cliff_list = cliff_list.reshape((24,24))
	np.save('./cliff_list.npy',cliff_list)

	inv_list = []
	for s in np.arange(0,len(cliff)):
		n = cliff_inv(cliff[s])
		inv_list.append(n)

	inv_list = np.array(inv_list)
	np.save('./inv_list.npy',inv_list)



