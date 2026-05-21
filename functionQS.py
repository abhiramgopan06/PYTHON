#1. Create a list of 10 numbers and print: 
# ○ the largest number 
# ○ the smallest number 

def numbers(a):
    print("Largest number:", max(a))
    print("Smallest number:", min(a))
list1 = [10, 25, 5, 40, 18, 7, 90, 12, 55, 3]
numbers(list1)


# 2. Write a program to count how many even numbers are in a list. 

def even_count(a):
    count = 0
    for i in a:
        if i % 2 == 0:
            count += 1
    print("Even numbers count:", count)
list1 = [10, 15, 22, 7, 8, 13, 24, 5, 18, 9]
even_count(list1)


# 5. Given a list of numbers, create a new list containing only odd numbers. 

def odd_numbers(a):
    odd_list = []
    for i in a:
        if i % 2 != 0:
            odd_list.append(i)
    print("Odd numbers list:", odd_list)
list1 = [10, 15, 22, 7, 8, 13, 24, 5, 18, 9]
odd_numbers(list1)


# 6. Find the second largest number in a list. 

def second_largest(a):
    a.sort()
    print("Second largest number:", a[-2])
list1 = [10, 25, 40, 15, 90, 60]
second_largest(list1)

