#1. Create a list of 10 numbers
#  the largest number 
#  the smallest number 
numbers = [12, 45, 7, 23, 89, 34, 2, 67, 90, 15]
largest = max(numbers)
smallest = min(numbers)
print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)

#2. Write a program to count how many even numbers are in a list.
numbers = [10, 15, 22, 33, 40, 55, 60, 73, 88, 91]
count = 0
for num in numbers:
    if num % 2 == 0: 
        count += 1
print("List:", numbers)
print("Number of even numbers:", count)

#4. Remove duplicate elements from a list. 
unique_numbers = {1,68,97,97,68}
print(unique_numbers)

#5. Given a list of numbers, create a new list containing only odd numbers. 
numbers = [10, 23, 45, 60, 77, 82, 91, 34, 55, 100]
count = 0
for num in numbers:
    if num % 2 != 0:
        count += 1
print("List:", numbers)
print("Number of odd numbers:", count)

# Given a list, swap the first and last elements. 
numbers = [10, 20, 30, 40, 50]
numbers[0],
numbers[-1] = numbers[-1], 
numbers[0]
print("After swapping:", numbers)
