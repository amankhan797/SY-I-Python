#Methodes to demonstrate operations on set (data structures).
set1={1,2,3,4,5,6,7}
set2={6,7,8,9,10}

#union in set
print(set1 | set2)
print(set2.union(set1))

#intersection in set
print(set1 & set2)
print(set1.intersection(set2))

#Difference in set
print(set1 - set2)
print(set2.difference(set1))

#Symmetric difference in set
print(set1 ^ set2)
print(set2.symmetric_difference(set1))
