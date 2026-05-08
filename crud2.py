students = []
while True:
    print('1. Display all Student details.')
    print('2. Add new student.')
    print('3. Edit student details.')
    print('4. Delete a student.')
    print('5. Exit.')
    choice = input('Enter your choice (1,2,3,4,5)....: ')
    match choice:
        case "1":
            if len(students) == 0:
                print('No students found. Add new one.')
            else:
                count = 1
                print(f"{'Sl. No.':<10}{'Name':<20}{'Roll No.':<10}{'Course':<15}")
                print('-' * 55)
                for student in students:
                    print(f"{count:<10}{student['name']:<20}{student['rollno']:<10}{student['course']:<15}")
                    count += 1
        case "2":
            name = input("Enter student's name: ")
            rollno = int(input("Enter student's roll no.: "))
            course = input("Enter student's course: ")
            students.append({'name': name,'rollno': rollno,'course': course})
        case "3":
            count = 1
            print(f"{'Sl. No.':<10}{'Name':<20}{'Roll No.':<10}{'Course':<15}")
            print('-' * 55)
            for student in students:
                print(f"{count:<10}{student['name']:<20}{student['rollno']:<10}{student['course']:<15}")
                count += 1
            rollno = int(input('Enter the roll no of the student you need to edit: '))
            name = input('Enter new name: ')
            course = input('Enter new Course: ')
            for student in students:
                if student['rollno'] == rollno:
                    student['name'] = name
                    student['course'] = course
                else:
                    print('No students found!!')
        case "5":
            print('Exiting....')
            break
        case _:
            print('Invalid Choice!!')