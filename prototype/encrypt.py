import cv2
import numpy as np
import random
import pickle
import sys

q = 829							# prime number < 1.84467 * 10^10

filename = sys.argv[1]

imarr = cv2.imread(filename)	# array generation


wupper = 10**9					# upper limit of w
wlower = 10						# lower limit of w
sh = imarr.shape

imarr = imarr.astype('uint64')

for i in range(sh[0]):
	for j in range(sh[1]):
		for k in range(sh[2]):
			w = random.randint(wlower, wupper)
			t =np.asarray(w*q)
			t = t.astype('uint64')
			imarr[i][j][k] += t

pickle.dump(imarr, open("encrypted.bin", 'wb'))