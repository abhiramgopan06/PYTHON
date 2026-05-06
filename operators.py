# classified into 6 groups
a = 90
b = 56
c = 60



# Arithmetic Operation (Mathematical Calculation)
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a//b) #Floop division
print(a%b) #Modulus
print(a**3) #Exponent



# Comparisun Operator
print(a==b)
print(a!=b)
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)

first_name = "Abhiram "
last_name = "Gopan"
print(first_name+last_name)
pattern = "#"
print(pattern*5)
print(first_name == last_name)
print(first_name <= last_name)
print(first_name < last_name)



# Logical Operator
# and
print(a>b and a>c)
print(a<b and a>c)
print(a>b and a<c)
print(a<b and a<c)
# or
print(a>b or a>c)
print(a<b or a>c)
print(a>b or a<c)
print(a<b or a<c)
# not
print( not b>c)
print( not b<c)



# Assignment Operator
count = 0
count+=5
count+=5
count-=5
count*=5
count/=5
print(count)



# Membership Operator
l1 = [25,36,98,7]
print(5 in l1)
print(25 in l1)

student1 = {
    "name" : "Abhiram",
    "age" : 18,
    "course" : "Python"
}
print("Abhiram" in student1)
print("name" in student1)
print("A" in first_name)
print("At" not in first_name,'not in')
# print(90 in a) error



# Identity Operator
student2 = {
    "name" : "Abhiram",
    "age" : 18,
    "course" : "Python"
}
student3 = student1
print(student1 == student2)
print(student1 is student2)
print(student1 is student3)
print(student1 is not student3)
