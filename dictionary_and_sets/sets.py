my_set=set() #Creating an empty set
my_set= {1,2,3,4,5,6,7}
print(my_set)

my_set.add(8)   #ADDING AN ELEMENT TO THE SET
print(my_set)   
my_set.remove(1)    #REMOVING AN ELEMENT FROM THE SET
print(my_set)   
print(len(my_set))  #PRINTING LENGTH OF SET

set1={2,3,4,6}
set2={2,1,5,7} 
print(set1.intersection(set2)) #intersection of set1 and set2
print(set1.union(set2))#union of set1 and set2
print({2,3}.issubset(set1)) #Testing subset
print(set1.issuperset({2,3})) #Tesing superset
