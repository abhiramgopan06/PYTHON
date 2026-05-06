import copy
names = ['Abhijit','Abhiram','Hari','Levin','Kevin']
names[0] = 'Abhijith'
# print(names[0])
# print(names[-1])

# print(names[1:3])
# print(names[-3:])

# data adding
# names.append(['Joppan','Karthik'])
# names.insert(2,'Karthik')
# names.extend(['Joppan','Karthik'])

# data removal
# names.pop()
# names.pop(2)
# names.remove('Abhijith')
# names.clear()
# del names
# del names[2]

# print(names)

numbers = [45,69,85,75,96,45,12,1,1,1,0,0,0,36,[36,56,89]]

print(numbers.count(75))
print(numbers.index(0))
# print(numbers.sort())
# n = numbers.copy
n = copy.deepcopy(numbers)
# numbers.reverse()
numbers[1]=6465
numbers[-1][0]=900
print(numbers)
print(n)

# list comprehension
# new_list = [expression for item in iterable if condition]
n = [25,36,89,78,53]
squared_numbers = [x*x for x in n if x%2!=0]
# squared_number = []
# for x in n:
#     if x%2!=0:
#         squared_numbers.append(x*x)
print(squared_numbers)