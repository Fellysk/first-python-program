#SETS
#store unique unorderd elements
#sets are mutable(remove or add elements)
#unorderd
#uses curly braces{}
#no indexing
#no duplicates

my_set = {1,2,3,4,5,6}
print(my_set)
print(type(my_set))

my_set_is = input()
print(f"my_set_is{my_set}")


#sets operation #UNION use "|"
my_union_set = {10,20,6, 30,40,50,5}
myset = my_union_set.union(my_set)
print(myset)


unionset = my_union_set| my_set
print(unionset)


#additing an elements in a sert
my_union_set.add(120)
print(my_union_set)

myseeet = {1,2,3,4,5,3,4,5}
print(myseeet)
myseeet= my_set.union(myseeet)
print(myseeet)

#intersection use &
int_set = my_union_set.intersection(my_set)
print(int_set)
inttset = myseeet & my_union_set
print(inttset)

#DIFFERENCE
myseeet= my_set.difference(my_union_set)
print(myseeet)

#symetric differnce