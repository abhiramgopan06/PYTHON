print("Welcom to python !!")
name= "Abhiram" #variable declaration

#Data-type in python
# 1. Numeric types
# int - (positive,zero,negative)
student_count = 56
#float = decimal numbers
avg_marks = 10.23
# complex
z = 2+3j

# 2. Sequence type
# str - string ('',"",''' ''',""" """)
course = 'Python Fullstack'
message = "Hello world"
address = """ 
Synnefo Solutions,
Iyyatil js.,
Near MG Road
"""

# list
number = [1,2,3,4,5]

# tuple
coordinates = (12,56)

# range
print(range(0,5))
print(range(1,101))

# 3. Set Type
# set
unique_numbers = {1,68,97,97,68}
print(unique_numbers)

# frozenset
fs = frozenset({654,84,4894})

# 4. Mapping Type
# dict (dictionary) : key_value pairs
{
    "key" : "value"
}

student = {
    "name" : "Abhiram",
    "age" : 18,
    "course" : "Python"
}

# 5.Boolean Type
# bool (True / False)
is_adult = True

# 6.Binary Type
# bytes
b = b"hello world"
print(b)

# bytearray
ba = bytearray(5)
print(ba)

# 7.None Type
# None

value = None

print(type(value))
print(type(name))
print(type(student))


# different variable same value
a = b = c = 10
print(a)
print(b)
print(c)

# different variable different values
x,y,z=10,20,30
print(x)
print(y)
print(z)

