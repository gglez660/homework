dna = 'ATGGCCTTT'
w = 0
list1= 'ACDEFGHIKLMNPQRSTVWY'
list2 = 'ACDEFGHIKLMNPQRSTVWY'
count = 0
for i in range(len(list1)):
        for j in range(len(list2)):
                if list1[i] != list2[j] and list2[j] != list1[i]:
                    print(list1[i],list2[j])
                    count += 1
        list2= list2[1:]
print(count)
