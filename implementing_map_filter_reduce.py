from itertools import izip as zip, count
from collections import Counter
import os
import time
import re
from functools import reduce
import multiprocessing as mp
start_time = time.time() ##

## Input Format:
#SEGMENTED LINE: [0]Promoter 	[1]TAG 	[2SampleName 	[3]Leader 	[4]LeaderLen 	[5]SegmentSeq 	[6]SegmentLen 	[7]Segment# 	[8]SegmentPostn

#get leader list
infile = '/mnt/ris-fas1a/linux_groups2/fantom5/capsnatch/source_data/raw_files/GCAAAAGCAGG_CAGE_Sequences_segmented.txt'
lead = 3

#list of leaders in order of abundance
leader_list = []
with open(infile, 'r') as inF:
	for line in inF:
		if '#' not in line:
		 	leader_list.append((line.split('\t'))[lead])
leader = Counter(leader_list)
#get leaders and counts
leader = Counter.most_common(leader)

leaders = []
leader_counts = []
for l in leader:
	leaders.append(l[0])
	leader_counts.append(l[1])
#leader_counts= sorted(leader.items())
#print("--- %s seconds ---" % (time.time() - start_time)) 
#44.6813750267 second

#/mnt/ris-fas1a/linux_groups2/fantom5/capsnatch
#list of files
file_list = []
path = '/mnt/ris-fas1a/linux_groups2/fantom5/Clustering/FLU_TIMECOURSE/bamfiles/'
dirs = os.listdir(path)
for fle in dirs:
	if '.sam' in fle:
		file_list.append(fle)
#print("--- %s seconds ---" % (time.time() - start_time))
#0.000220060348511 seconds

def Locate_Leaders(filename):
	bamfiles_list = []
	bamfiles_list2 = []
	with open(filename, 'r') as inF:
		for line in inF:
			if 'VHE' in line:
				line = line.split('\t')
				bamfiles_list.append(line[9])
				bamfiles_list2.append([line[9], line[2], line[3]])
	#print("--- %s seconds ---" % (time.time() - start_time))
	#6.47017002106 seconds
	#namefile
	#in_file = os.path.abspath(filename)
	donor =  (re.split('%20|%3a|%29', filename))[8]
	sample =  (re.split('%20|%3a|%29', filename))[10]
	output = ('/mnt/ris-fas1a/linux_groups2/fantom5/capsnatch/%s_%s_leader.tsv')%(sample,donor)
	#if os.path.isfile(output) == False:
	#	print ('%s_%s_leader.tsv has been created')%(sample,donor)
	o = open(output, 'ab+')
	for i in range(0, len(leaders[1000:5000])):
		if len(leaders[i]) > 8 :
			value = list(map(lambda x: str(x).startswith(leaders[i]), (bamfiles_list)))
			indexes = ([y for y, j in zip(count(), value) if j == True])
			location = list(map(lambda x : str((bamfiles_list2[x])[1]) + ' ' + str((bamfiles_list2[x])[2]) , indexes))
			total = str(len(location))
			location = Counter(location)
			location = Counter.most_common(location)
			o.write(str(leaders[i]) + '\t' + total)
			for l in location:
				o.write('\t' + str(l[0]) + '-' + str(l[1]))
			o.write('\n')
				#print("--- %s seconds ---" % (time.time() - start_time))

pool = mp.Pool(processes=12)
results = pool.map(Locate_Leaders, file_list)

#0-1000 done :) 
