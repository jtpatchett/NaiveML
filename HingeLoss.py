# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:24:24 2020

@author: jxp52
"""

import sys
import random


def dprod (wi, xi):
	dp = 0
	for i in range(0, len(wi), 1):
		dp+= wi[i] * xi[i]
	return dp

datafile = sys.argv[1]
#datafile = "GDdata.csv"
#datafile = "breast_cancer.data"
#datafile = "ionosphere.data"
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
c = float(sys.argv[5])
#c = .01
# stop = .001
#stop = .001
#labelfile = "GDlabels.csv"
#labelfile = "breast_cancer.trainlabels.0"
#labelfile = "ionosphere.trainlabels.0"
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


for i in range(0, rows, 1):
	if (trainlabels.get(i) == 0):
		trainlabels[i] = -1

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
			dotprod = dprod(w, data[i])
			hingeLoss = trainlabels.get(i)*dprod(data[i],w)
			#technically the gradient (xi *yi)
			for j in range(0, cols, 1):
				if (hingeLoss >= 1.0):
					dellf[j] += 0.0
				else:
					dellf[j] += trainlabels.get(i) * data[i][j]

	
	for j in range(0, cols, 1):
		w[j] = w[j] + eta * dellf[j]
		
	error1 = 0
	normw = 0
	for j in range(0, cols, 1):
		normw += w[j] **2
	normw = normw **(1/2)
	for i in range(0, rows, 1):
		if (trainlabels.get(i) != None):
			error1 += max(1-trainlabels.get(i)*dprod(w, data[i]),0)
	if (abs(error2-error1) < stop):
		break
	error2 = error1

normw = 0
for j in range(0, cols, 1):
	normw += w[j] **2
normw = normw **(1/2)


for i in range(0, rows, 1):
	if (trainlabels.get(i) == None):
		dp = dprod(w, data[i])
		if (dp > 0.0):
			print(1, i)
		else:
			print(0, i)
