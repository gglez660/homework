seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
for i in range(len(seq) - (w-1)):
        gc=0
        codon = seq[i:i+11]
        for j in range(w):
                if (seq[i+j] == 'G' or seq[i+j] == 'C'):
                        gc += 1
        print(i,codon,f'{gc/(len(codon)):.4f}')
