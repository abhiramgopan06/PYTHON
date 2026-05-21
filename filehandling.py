# open('path','mode')   (modes x -> create r -> read w -> write a -> append)

# file = open('sample.txt','x')
# file.write('data')

# file = open('sample.txt','w')
# file.write('MERN, Python, Flutter')

# file = open('sample.txt','a')
# file.write('\nNetworking, Cyber Security')

# file = open('sample.txt','r')
# data = file.read()
# print(data)

# file.close()

# with open('sample.txt','r') as file:
#     data = file.read()
#     print(data)

# with open('sample.txt','a') as file:
#     file.write('\nDevops')

# with open('sample.txt','r') as file:
#     data = file.read()
#     print(data)

# try:
#     with open('sample2.txt','r') as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print('No such files!!')

import os

# os.remove('name.txt')

# os.mkdir('photos')
os.rmdir('photos')