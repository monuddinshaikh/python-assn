# Single leval inheritance.
class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

obj = Dog()
obj.eat()
obj.bark()

# Multilevel inheritance.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car charging")

obj = ElectricCar()
obj.start()
obj.drive()
obj.charge()

# Multiple inheritance. 
class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def child_skill(self):
        print("Child: Coding")

obj = Child()
obj.skills()
obj.child_skill()

#Hierarchical inheritance.
class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def circle(self):
        print("This is a circle")

class Square(Shape):
    def square(self):
        print("This is a square")

c = Circle()
s = Square()

c.display()
c.circle()

s.display()
s.square()

#Hybrid inheritance.
class Person:
    def show_person(self):
        print("This is a Person")

class Employee(Person):
    def show_employee(self):
        print("This is an Employee")

class Student(Person):
    def show_student(self):
        print("This is a Student")

class Intern(Employee, Student):
    def show_intern(self):
        print("This is an Intern")

obj = Intern()
obj.show_person()
obj.show_employee()
obj.show_student()
obj.show_intern()

#Super() use of inheritance.
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("Child constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

obj = Child("Rahul", 20)
obj.display()