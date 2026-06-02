import re

# re.match('pattern','data') match object or None

s1 = "Hello, world"
s2 = 'Hello, world. Hello python, Hello django'

p1 = r'Hello'   # raw string

# print('hello.\\nworld')
# print(r'hello.\\nworld')
# print(re.match(p1, s1).group())
# print(re.search('@', 'example@gmail.com'))
# print(re.match(p1, s2))
# print(re.findall(p1, s2))
# print(re.findall(p1,s2))
# Special characters used with regexp

# ^ starting of a string
# print(re.search(r'^Hello',s1))
# print(re.search(r'^Hello',s2))

# $ ending of a string
# print(re.search(r'world$',s1))
# print(re.search(r'world$',s2))

# . any one character
# print(re.search(r'cat.','i love catsygfhhkjlk;lj;jh'))
# print(re.search(r'cat.','i love cat99'))
# print(re.search(r'cat.','i love cat!!'))
# print(re.search(r'cat.','i love cat#'))

# * 0 or more
# print(re.search(r'cats*','i love cat'))
# print(re.search(r'cats*','i love catssssssss'))

# + 1 or more
# print(re.search(r'cats+','i love cat'))
# print(re.search(r'cats+','i love catssssssss'))

# ? 0 or 1
# print(re.search(r'cats?','i love cat'))
# print(re.search(r'cats?','i love cats'))
# print(re.search(r'cats?','i love catssssssss'))

# [] included
# print(re.search(r'[cb]at?','i love cat'))
# print(re.search(r'[cb]at?','i love bat'))

# [^] not included
# print(re.search(r'[^cb]at?','i love cat'))
# print(re.search(r'[^cb]at?','i love bat'))
# print(re.search(r'[^cb]at?','i love mat'))
# print(re.search(r'[^cb]at?','i love pat'))

# - range
# print(re.search(r'[a-z]','4552874754356'))
# print(re.search(r'[a-m]+','455287tom4356'))
# print(re.search(r'[A-Z]+','455287tom54356'))
# print(re.search(r'[0-9]+','45528tom54356'))
# print(re.search(r'[0-6]+','45528tom54356'))

# \escape character

# print(re.search(r'\.','example@gmail.com'))
# print(re.search(r'\.[a-z]+$','example@gmail.com'))

# \d - digit  \D - non-digits
print(re.search(r'[\d]{5}','45528975554356'))
print(re.search(r'[\d]{5,10}','455289765554356'))
print(re.search(r'[\d]{5,10}','455'))

# \w - world characters | \W - non-digits
print(re.search(r'[\w]{5}', 'hello123'))
print(re.search(r'[\w]{5,10}', 'python_2026'))
print(re.search(r'[\w]{5,10}', 'abc'))

# \s - whitespace  |  \S - non-whitesplce
print(re.search(r'\S', 'Hello World'))
print(re.search(r'\s', 'Hello  World'))
print(re.search(r'\s', 'HelloWorld'))

# re.sub('pattern','character','string')
print(re.sub(r'b','*','i am bob'))
print(re.sub(r'\d','*',"my number is 89876433345"))

# re.split('pattern','string')
print(re.split(r',','Apple,Grapes,Orange'))


print(re.search(r'^[6-9]\d{9}$','8552894356'))



