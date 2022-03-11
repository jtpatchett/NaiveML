import sys
import random


#datafile = "GDdata.csv"
datafile = sys.argv[1]
#k = 2
k = sys.argv[2]
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


col = [0 for i in range(0, cols, 1)]
split = [col for i in range(0, rows//2, 1)]
#split = []
value = 0

for i in range(0, rows//2, 1):
	value = random.randrange(1, rows-1)
	split[i] = data[value]
clusters = {}

prev = [[0]*cols for i in range(k)]
meanDist = [0 for i in range(0, k, 1)]
#initializing lists
n = [0.1 for i in range(0, k, 1)]
distance = [0.1 for i in range(0, k, 1)]

tot_dist = 1000
while ((tot_dist) > 0):
	for i in range(0, rows, 1):
		distance = []

		for val in range(0, k, 1):
			distance.append(0)

		for val in range(0, k, 1):
			for j in range(0, cols, 1):
				distance[val] += ((data[i][j] - split[val][j])**2)

		for val in range(0, k, 1):
			distance[val] = (distance[val])**0.5

		mindist = 0
		mindist = min(distance)
		for val in range(0, k, 1):
			if(distance[val] == mindist):
				clusters[i] = val
				n[val] += 1
				break
	split = [[0]*cols for g in range(k)]
	for i in range(0, rows, 1):
		for val in range(0, k, 1):
			if(clusters.get(i) == val):
				for j in range(0, cols, 1):
					dist = split[val][j]
					point = data[i][j]
					split[val][j] = dist + point
	for j in range(0, cols, 1):
		for val in range(0, k, 1):
			split[val][j] = split[val][j]/n[val]
	n = [0.1]*k
	meanDist = []
	for val in range(0, k, 1):
		meanDist.append(0)
	for val in range(0, k, 1):
		for c in range(0, cols, 1):
			meanDist[val] += float((prev[val][c]-split[val][c])**2)

		meanDist[val] = (meanDist[val])**0.5

	prev = split
	tot_dist = 0
	for i in range(0, len(meanDist), 1):
		tot_dist += meanDist[i]
for i in range(0, rows, 1):
	print(clusters[i], i)