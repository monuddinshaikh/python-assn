tup1 = (10,20,"hello",3.14,'r',True)
tup2 = (20,30,"Python",12.20,'v',False)

tup = tup1 + tup2
print(tup)

# Convert into tuple from list.
l = list(tup1)
print(l)
l.append("Ravi")

t = tuple(l)
print(t)

# Access the value with index.
print(tup[0])
print(tup[2])
print(tup[5])
print(tup[1])