# def function_name(parameters):
#     #block of code
#     return 'value'

# function_name(arguments)

def add(a,b):
    return a+b
x = 12
y = 56
result = add(x,y)
print(result)


# Default parameter
def greet(user = "Guest"):
    print(f"Welcome, {user}")
greet('Alan')
greet()

# Keyword Arguments
def getDetails(name,age):
    print('Name: ',name)
    print('Age: ',age)
getDetails(age=15,name='Alan')

# Arbitrary Arguments
def numbers(*args):
    print('Numbers',args)
numbers(10,12,3,45,8,79,63,71,10,7)

# Arbitrary Keyword Argument
def details(**kwargs):
    print('Details',kwargs)
details(name='Abhiram',age=18,course='Python')

# lambda function

sum = lambda x,y:x+y
print(sum(56,89))

square = lambda x:x*x
print(square(2))
print(square(9))
print(square(74))
print(square(15))
print(square(11))

l1 = [13,56,31,9,8,7,9,67]
result = list(map(lambda x:x*x,l1))
print(result)

odd_numbers = list(filter(lambda x:x%2!=0,l1))
print(odd_numbers)