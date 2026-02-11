# Student data!
student = {
    "name" : "Ravi",
    "Age" : 21,
    "City" : "Jaipur",
    "Course" : "Pyhton"
}

# Updating after value!
student["City"] = "Himatnagar"
student["Course"] = "Django"

# Updating after student data.
print(student)

# Two merge list using loop in dictionary!
key = ["name","Age", "Course", "City", "College", "Cgpa"]
value = ["ravi", 21, "Python", "Himatnagar", "Vidhyanagari", 7.31]

my_dict = {}

for i in range(len(key)):
    my_dict[key[i]] = value[i]

print("Merge dictionary", my_dict)