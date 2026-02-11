name = ["Ravi", "sahil", "abhay","dipen"]

print("list in name!")
for names in name:
    print(names)

# using sort.
numbers = [5, 7, 8, 9, 26, 25, 12,15]

print("original number list: ",numbers)

numbers.sort()
print("After using sorting number: ",numbers)

numbers = [5, 7, 8, 9, 26, 25, 12,15]

sorted_list = sorted(numbers)
print("sorted list using sorted():",sorted_list)
print("Original list remains unchanged: ",numbers)

# iterate element.
number = [1, 2, 3, 4, 5, 6,7]
print("Element are: ")

for num in number:
    print(num)

# use blank list operation.
list_num = []

for i in range(5):
    element = int(input(f"Enter element{i+1}: "))
    list_num.append(element)

print("Final list is: ",list_num) 
   