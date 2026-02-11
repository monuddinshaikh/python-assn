list = ["hello", 3.14, 13, True, 'r']
print(list)

# Append method use.
list.append(10)
print(list)

# Insert method use.
list.insert(1,12)
print(list)

# pop method use.
poped_value = list.pop(1)
print("poped value is: ",poped_value)
print("After poped value in list: ",list)

# remove method use.
list.remove('r')
print(list)

# practicle example:
#1. list using insert.
list2 = [10, "hello",'t', True, 12.32]
list2.insert(0,18)
print(list2)

#2. list using append.
list2.append("Ravi")
print(list2)

#3.list using pop.
poped_value = list.pop(2)
print("poped value is:",poped_value)
print("After poped value in list: ",list2)

#4. list using remove.
list2.remove(12.32)
print(list2)
