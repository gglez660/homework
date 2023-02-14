# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys
p=[]
for val in sys.argv[1:]:
	p.append(float(val))
avg = (sum(p)/len(p))

sum = 0
for i in p:
	sum += (i- avg) **2 
variance = sum/ len(p)
std_dev= variance ** .5
median = None

p.sort()

if len(p) % 2 == 0:
	median = (p[int(len(p)/2)] + p[int(len(p)/2)-1]) / 2
else:
	median = p[int(len(p)/2)]

	
	
print(f'Count:{len(p)}')
print(f'Minimum: {min(p):.1f}')
print(f'Maximum: {max(p):.1f}')
print(f'Mean: {avg:.3f}')
print(f'Std. dev: {std_dev:.3f}')
print(f'Median: {median:.3f}')
	
'''
median = (p[middle] + p[middle -1]) // 2
avg = (sum(p)/len(p))
sum = 0
for i in p:
	sum += (i- avg) **2 
variance = sum/ len(p)
std_dev= variance ** .5

p.sort()
middle = (int(len(p) / 2))
median = None

if len(p) % 2 == 0:
	median = (p[middle] + p[middle -1]) // 2
else:
	median = p[middle]
print(f'Count:{len(p)}')
print(f'Minimum: {min(p):.1f}')
print(f'Maximum: {max(p):.1f}')
print(f'Mean: {avg:.3f}')
print(f'Std. dev: {std_dev:.3f}')
print(f'Median: {middle:.3f}')
'''
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""

