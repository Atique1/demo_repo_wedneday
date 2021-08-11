# sets = unordered, mutable, no duplicates

# a set is also crated with curly braces {} like dictionar but dont have key-value pairs
my_set = {2,1,345,46,23}
print (my_set)  # since set is unordered ther is no sequence of showing output

# creat a set with string
my_set2 = set('hello')
print (my_set2) # out put will show only one l instead of 2.

# create a set with lists
my_set4 = set([123,35,4567,68,789,3])

# create an empty sets
my_set3 =set()

# add value to a set
my_set3.add(2)
my_set3.add(45)
my_set3.add('atique')
print (my_set3)

# remove a element from set
my_set3.remove('atique')
print (my_set3)

# remove a element from set, if not found don't through any exception
my_set3.discard('atique')
print (my_set3)

# empty set
my_set3.clear()
print (my_set3)

# delete element randomly/arbitrary
my_sets7 = {2,3,8.9,4}
print (my_sets7)
my_set4.pop()
print (my_set4)

# iterate a sets with for loop
for i in my_set4:
    print (i)
    
# check a element from sets
if 789 in my_sets7:
    print ('yes')
else:
    print ('no')
    
# union two or more sets
odds ={1,3,5,7,9}
evens = {0,2,4,6,8,}
prime = {1,2,3,5,7,11}

u = odds.union(evens)
print (u)

# intersection of two or more sets
i_ntersection = odds.intersection(prime)
print (i_ntersection)

# find difference between two sets
setA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 3, 5, 7}

d = setA.difference(setB)
print (d)

# modify the original sets
setC = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {11, 3, 50, 7}

setC.update(setD)
print (setC)

# only element found in both  sets
setE = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
setF = {11, 3, 50, 7}

setE.intersection_update(setF)
print (setE)

# remove the common from another sets and then keep it's own set elemets
setG = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
setH = {11, 3, 50, 7}

setG.difference_update(setH)
print (setG)

# remove the commonalities and then join uncommon element to the selected sets
setI = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
setJ = {11, 3, 50, 7}

setI.symmetric_difference_update(setJ)
print (setI)

# subset, superset, disjoint(no same elements among sets)
setAA = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
setBB = {0, 1, 2, 3}

print (setAA.issubset(setBB)) # subset example
print (setBB.issubset(setAA))

print (setAA.issuperset(setBB)) # superset example

print (setAA.isdisjoint(setBB)) # disjoint example

# copy sets
setDD = setAA # here it will only assigh from one to anotehr. both points to the same sets
setCC = setAA.copy()
setDD = set(setAA) # this also make an actual copy
print (setCC)

# frozen sets - it is the immutable version of normal sets
a = frozenset([1,5,56,234])
    # a.add(2) can not be possible. but we can use union, intersectioln, and difference method will work
print (a)









