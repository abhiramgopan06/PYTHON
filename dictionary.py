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