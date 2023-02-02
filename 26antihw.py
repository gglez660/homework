dna = 'ACTGAAAAAAAAAAA'

dna2= dna[::-1]

for i in range(len(dna2)):
    nt = dna2[i]
    if nt == 'A':
        print('T',end = '')
    if nt == 'C':
        print('G', end = '')
    if nt == 'T':
        print('A', end = '')
    if nt == 'G':
        print('C', end = '')
print(dna2[i])
