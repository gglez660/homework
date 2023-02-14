# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import sys
import random

genomelength = int(sys.argv[1])
readlen = int(sys.argv[2])
readnum = int(sys.argv[3])
genome = []
for i in range(genomelength):
	addnucleotide = random.choice("ACGT")
	genome.append(str(addnucleotide))

coverage = []
for i in range(genomelength):
	coverage.append(0)
for i in range(readnum):
	addread = 0
	addread = random.randint(1,len(coverage))
	for j in range(readlen):
		if addread + j > genomelength:
			break
		else:
			coverage[addread + j -1] += 1 
print(sum(coverage)/ len(coverage))
print(max(coverage))
print(min(coverage))

	




'''
for i in range(readnum):
	start = random.randint(0,len(genome) - readnum)
	print(start)
	for j in range(readlen):
		genome[j+start] += 1
print(genome)
print(genome.max(), genome.min())
avg = sum(genome)/len(genome)
print(avg)
python3 32xcoverage.py 1000 100 100
5 20 10.82375
'''
