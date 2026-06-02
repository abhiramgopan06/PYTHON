# class is a blueprint of object
# object is an instance of class

class Student:

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    def greet(self,message):
        print(f"Welcome, {self.name}, {message}")

print('creating s1')
s1 = Student('Amal',6)

print('creating s2')
s2 = Student('Arun',7)

print(s1.name)
print(s1.rno)

print(s2.name)
print(s2.rno)

s1.greet('Good morning!')
