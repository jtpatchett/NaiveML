# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:24:24 2020

@author: jxp52
"""

import sys
datafile = sys.argv[1]
#datafile = "breast_cancer.data"
f = open(datafile)
data = []
i = 0
l = f.readline()

while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

labelfile = sys.argv[2]
#labelfile = "breast_cancer.trainlabels.0"
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
m0 = []
for j in range(0, cols, 1):
	m0.append(0.1)
m1 = []
for j in range(0, cols, 1):
	m1.append(0.1)
for i in range(0, rows, 1):
	if(trainlabels.get(i) != None and trainlabels[i] == 0):
		for j in range(0, cols, 1):
			m0[j] = m0[j] + data[i][j]
	if(trainlabels.get(i) != None and trainlabels[i] == 1):
		for j in range(0, cols, 1):
			m1[j] = m1[j] + data[i][j]

for j in range(0, cols, 1):
	m0[j] = m0[j]/n[0]
	m1[j] = m1[j]/n[1]

std0 = []
std1 = []

for i in range(0, cols, 1):
	std0.append(0)
	std1.append(0)

for i in range(0,rows,1):
	if (trainlabels.get(i) != None and trainlabels[i] == 0):
		for j in range(0,cols, 1):
			std0[j] = std0[j] + (data[i][j] - m0[j])**2

for i in range(0,rows,1):
	if (trainlabels.get(i) != None and trainlabels[i] == 1):
		for j in range(0,cols, 1):
			std1[j] = std1[j] + (data[i][j] - m1[j])**2

for j in range(0, cols, 1):
	std0[j] = (std0[j]/n[0])**(1/2)
	std1[j] = (std1[j]/n[1])**(1/2)
	
for i in range(0, rows, 1):
	if(trainlabels.get(i) == None):
		d0 = 0
		d1 = 0
		for j in range(0, cols, 1):
			d0 = d0 + (( m0[j] - data[i][j])/std0[j])**2
			d1 = d1 + (( m1[j] - data[i][j])/std1[j])**2
		if(d0 <d1):
			print("0",i)
		else:
			print("1",i)