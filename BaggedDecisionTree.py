# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:24:24 2020

@author: jxp52
"""

import sys
from random import randrange


datafile = sys.argv[1]
#datafile = "GDdata.csv"
#datafile = "breast_cancer.data"
#datafile = "bagData.txt"
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
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()

labelfile = sys.argv[2]
#eta = sys.argv[3]
#eta = .001
#stop = sys.argv[4]
#c = sys.argv[5]
#c = .01
# stop = .001

#labelfile = "GDlabels.csv"
#labelfile = "breast_cancer.trainlabels.0"
#labelfile = "bagLabels.txt"
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

negcount = 0
for i in range(0, rows, 1):
	if (trainlabels.get(i) == 0):
		trainlabels[i] = -1

bestGini = 100000
split = 100000
colnumber = 10
testDS = []
trainDS = []
trRows = 0
rTrLabels = dict()
Indices =[]
for i in range(0, rows, 1):
	if (trainlabels.get(i) == None):
		testDS.append(data[i])
		Indices.append(i)
	else:
		trainDS.append(data[i])
		rTrLabels[trRows] = trainlabels.get(i)
		trRows +=1

rows = trRows

votingCols = []
for count in range(0,100,1):
	bestGini = 1000
	split = 1000
	trainBS = []
	labelBS = dict()
	for val in range(0,rows,1):
		value = randrange(rows)
		trainBS.append(trainDS[value])
		labelBS[val] = rTrLabels[value]
	negcount = 0
	for i in range(0,rows,1):
		if (labelBS.get(i) == -1):
			negcount += 1
	
	for j in range(0,cols, 1):
		colval = [[trainBS[i][j], i] for i in range (0, rows,1) ]
		colval = sorted(colval, key = lambda x: x[0], reverse = False)
		for i in range(0,rows-1, 1):
			lsize = i+1
			rsize = rows - (i+1)
			lp =0
			for k in range(0, i+1,1):
				if(labelBS.get(colval[k][1]) == -1):
					lp += 1
			rp = negcount - lp
			gini = (lp/rows) * (1-lp/lsize) + (rp/rows)*(1-rp/rsize)
			if (gini < bestGini):
				bestGini = gini
				split = colval[i][0] + (colval[i+1][0] - colval[i][0])/2
				colnumber = j
				if (lp >= rp):
					lower = -1
				else:
					lower = 1
	votingCols.append([split, colnumber, lower])

for i in range(0,len(testDS),1):
	prediction = 0
	for j in range(0, len(votingCols),1):
		if (testDS[i][votingCols[j][1]] < votingCols[j][0]):
			prediction += votingCols[j][2]
		else:
			prediction += votingCols[j][2] *-1
# 	print(prediction, Indices[i])
	if (prediction >= 0):
		print(1,Indices[i])
	else:
		print(0, Indices[i])
	