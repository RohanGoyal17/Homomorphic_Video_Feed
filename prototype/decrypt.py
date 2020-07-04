import cv2
import pickle
import sys
import numpy as np

fname = 'enc.bin'
q = 829
q = (np.asarray(q)).astype('uint64')
dec_arr = pickle.load(open(fname, 'rb'))%q
dec_arr = dec_arr.astype('uint8')
#pickle.dump(dec_arr, open("dec.bin", 'wb'))

sh = dec_arr.shape
for i in range(sh[0]):
	for j in range(sh[1]):
		for k in range(sh[2]):
			if dec_arr[i,j,k] in range(0,256):
				pass
			elif dec_arr[i,j,k] in range(256,700):
				dec_arr[i,j,k] = 0
			else:
				dec_arr[i,j,k] = 255
cv2.imwrite("out.jpg", dec_arr)
