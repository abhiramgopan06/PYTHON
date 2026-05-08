student = {
    "rollno":12,
    "name":"Rony",
    "class":12,
    "name":"Rony Mathew"
}
student['class'] = 'XIIth'
student['age'] = 17
student['age'] = 18
print(student)
print(student['class'])

employee = dict(name='Athul',role='Frontend Developer',department='Software')
print(employee)

for x in student:
    print(f"{x} = {student[x]}")

student.update({"rollno":2})
student.update({"marks":[56,89,70]})
print(student.get('marks'))

    # student.pop('age')
    # student.popitem()

    # del student['rollno']
    # student.clear()

print(student.keys())
print(student.values())
print(student.items())
for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(f"{key} = {value}")


a = 1,2,3
n1,n2,n3 = a
print(n1)
print(n2)
print(n3)