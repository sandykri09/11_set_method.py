"""set is represented by {} with element inside it but we cannot represent empty set ."""
"if we keep empty set {} it will treated as dictionary(dict)"
"set can contain several data types in it but we cannot have a list and one more set inside it."
"set cannot have one more set inside it. set is mutable , modifications can be made "
'we can add or remove from set but frozenset is immutable .'
'we cannot add or remove elements in it.  set is inordered '

# e={}
# print(e,type(e))  # {} <class 'dict'>

# v={1,2.6,"Hello",("hi",2)}
# print(v,type(v)) # "set"
# print(v) # {1,2.6,'Hello',('hi',2)}

# n={10,20,30}
# print(n[1])   # TypeError: 'set' object is not subscriptable 

# a={1,2,3}
# b='hello',10,20,30
# a.add(b)
# print(a)

# b={1,5,7}
# b.clear()
# print(b)  # set()

# a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
# print(a.intersection(b))  # {3}
# print(a.intersection(c))  # set()
# print(a.intersection(d))  # {1}
# print(b.intersection(d))  # {4}

# a={1,2,3,'hello'}
# b={4,3,5,'hey'}
# print(a.union(b)) #{1,2,3,4,5,'hey','hello'}
# print(b.union(a)) # {1,2,3,4,5,'hey','hello'}

# a={1,2,3}
# b={4,3,5}
# c={4,3,7}
# a.update(b)
# a.update(c)
# print(a)

# a={5,10,20,25,30}
# b={10,21,5}
# print(a.difference(b)) # {25,20,30}
# print(b.difference(a)) # {21}
# print(a-b)  # {25,20,30}
# print(b-a)  # {21}

# z={55,56,57,73,45,23}
# z.discard(44)
# print(z) # {55,23,56,73,45,57}
# z.discard(73)
# print(z) # {55,23,56,45,57}

# v={26,7,11,4,23}
# v.pop()
# print(v)  # {23,7,26,11}

# A={1,2,3,4}
# B={5,6,7}
# C={4,5,6}
# print('Are A and B disjoint?', A.isdisjoint(B))  # True
# print('Are A and c disjoint?', A.isdisjoint(C))  # False
# print('Are B and C disjoint?', A.isdisjoint(C))  # False

# A={1,2,3}
# B={1,2,3,4,5}
# C={1,2,4,5}
# print(A.issubset(B)) # True
# print(B.issubset(A)) # False
# print(A.issubset(C)) # False
# print(C.issubset(B)) # True

# print(dir(set))

"""remove set type"""

# a={8,9,10,12,14}
# a.remove(140)
# print(a)  # KeyError: 140

"""issuperset"""

# a={8,9,10,12,14}
# b={10,14,15,1}
# print(a.issuperset(b))  # False

a={8,9,10,12,14}
b={8,9,10}
print(a.issuperset(b))  # True
print(b.issuperset(a))  # False