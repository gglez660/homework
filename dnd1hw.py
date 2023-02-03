import random
sum = 0
n = 1000000
for i in range(n):
    x = random.randint(1,10)
    if x == 1:
        x = 2
    sum = sum +x
print(sum)
print(sum/n)

#.1
