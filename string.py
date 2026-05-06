# string methods

str1 = "hello world"
# print(str1)
# print(str1[0])
# print(str1[7])
# print(str1[-1])
# string slicing [strrt:end:step]
# print(str1[1:7])
# print(str1[1:7:3])
# print(str1[::3])

# case changeing
# print(str1.upper())
# print(str1.lower())
# print(str1.capitalize())
# print(str1.title())

# searching
text1 = "python programming"
# print(text1.find('thon'))
# print(text1.index('pro'))

text2 = "I like Javascript"
# print(text2.replace('Javascript','python'))

l1 = ['apple','orange','banana']
# print("-".join(l1))

text3 = 'apple,orange,banana'
# print(text3.split('a'))

text4 = "   i like python   "
print(f"{text4.strip()}")
print(f"{text4.lstrip()}2")
print(f"{text4.rstrip()}2")


text5 = '2345 67t'

# print(text4.isspace())
# print(text2.isalpha())
# print(text5.isdigit())
# print(text5.isalnum)

print(text1.startswith("python"))
print(text2.endswith("script"))

print(text3.count('a'))

n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))
a1 = n1 + n2 +n3
print(f'The Answer is {a1}')