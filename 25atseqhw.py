import random
n = 30
at = 0
seq = ''

for i in range(n):
    r= random.randint(1,10)
    if r<=3:
        seq += 'A'
        at +=1
    if r<=6 and r>3:
        seq += 'T'
        at +=1
    if r>6 and r<=8:
        seq += 'C'
        at +=1
    if r>8 and r<=10:
        seq += 'G'
        at +=1
print(30,seq, at/n)

#with significant help and thanks to Ricky! as with all my other homework files, ricky was a lifesaver and patiently helped me many concepts. I'm indebted to him 
