# method overloading.
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()

print(obj.add(5))        
print(obj.add(5, 10))    
print(obj.add(5, 10, 15))

# method overriding.
class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        print("This is Child class method (Overridden)")

obj = Child()
obj.show()

