# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
import math
import sys

p = []
for val in sys.argv[1:]:
	p.append(float(val))
assert(math.isclose(sum(p),1.0))	
shannon = 0 
for i in range(len(p)):
	shannon = p[i] * math.log2(1/p[i]) + shannon
	
print(f'{shannon:.3f}')
	
