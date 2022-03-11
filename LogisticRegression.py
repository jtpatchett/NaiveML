# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:52:45 2020

@author: jxp52
"""

# -*- coding: utf-8 -*-

import sys
import random
import math

def dprod (wi, xi):
	dp = 0
	for i in range(0, len(wi), 1):
		dp+= wi[i] * xi[i]
	return dp

def sigmoid(xi, wi):
	return (1/(1+math.exp(-dprod(xi,wi))))

datafile = sys.argv[1]
#datafile = "GDdata.csv"
#datafile = "breast_cancer.data"
#datafile = "ionosphere.data"
#datafile = "climate.data"
f = open(datafile)
data = []
i = 0
l = f.readline()

while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	l2.append(1.0)
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

labelfile = sys.argv[2]
eta = float(sys.argv[3])
#eta = .001
stop = float(sys.argv[4])
#c = float(sys.argv[5])
#c = .01
#stop = .001
#stop = .00000001
#labelfile = "GDlabels.csv"
#labelfile = "breast_cancer.trainlabels.0"
#labelfile = "ionosphere.trainlabels.0"
#labelfile = "climate.trainlabels.0"
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	l = f.readline()
	n[int(a[0])] += 1
	
f.close()

w = []
for j in range(0, cols, 1):
	w.append(.02 * random.random() - .01)
#w0 = .02 *random.random() -.01



#error of the previous objective, initialized to zero
error2 = 2000

for k in range(0, 500000):
	dellf = []
	
	dellf0 = 0
	for i in range(0,cols,1):
		dellf.append(0)
	for i in range(0, rows, 1):
		hingeLoss = 0
		if (trainlabels.get(i) != None):
			#dotprod = dprod(w, data[i])*(-1)
			sig = trainlabels.get(i) - sigmoid(data[i], w)

			for j in range(0, cols, 1):
				dellf[j] += sig * data[i][j]

	
	for j in range(0, cols, 1):
		w[j] = w[j] + eta * dellf[j]
	#w0 = w0 + eta * dellf0
#error of the current objective
	error1 = 0

	#print(w[j])
	for i in range(0, rows, 1):
		if (trainlabels.get(i) != None):
			#error1 += (trainlabels.get(i) - (dprod(w, data[i]))) **2
			error1 += - trainlabels.get(i) * math.log(sigmoid(data[i], w)) - (1 - trainlabels.get(i)) * math.log(1-sigmoid(data[i],w)) 
	if (abs(error2-error1) < stop):
		break
	error2 = error1

normw = 0
for j in range(0, cols, 1):
	normw += w[j] **2
	#print(w[j])
normw = normw **(1/2)
#print(normw)

for i in range(0, rows, 1):
	if (trainlabels.get(i) == None):
		dp = sigmoid(data[i],w)
		if (dp > 0.5):
			print(1, i)
		else:
			print(0, i)
