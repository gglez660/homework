
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
counter = 0

for i in range(len(dna)):
	if dna[i] == 'G' or dna[i] == 'C':
		counter +=1
print (f'{counter/(len(dna)):.2f}')
