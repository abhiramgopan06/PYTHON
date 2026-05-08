names = []
while True:
    print('1. Display all names.')
    print('2. Add new name.')
    print('3. Edit a name.')
    print('4. Delete a name.')
    print('5. Exit.')
    choice = input('Enter your choice (1,2,3,4,5)....: ')
    match choice:
        case "1":
            if len(names) == 0:
                print('No names found. Add new one.')
            else:
                count = 1
                for name in names:
                    print(f"{count}. {name}")
                    count += 1

        case "2":
            name = input('Enter the name : ')
            names.append(name)

        case "3":
            count = 1
            for name in names:
                print(f"{count}. {name}")
                count += 1

            index = int(input('Enter the index of the name you want to edit : '))
            new_name = input('Enter new name : ')
            names[index - 1] = new_name

        case "4":
            count = 1
            for name in names:
                print(f"{count}. {name}")
                count += 1

            index = int(input('Enter the index of the name you want to delete : '))
            names.pop(index - 1)

        case "5":
            print('Exiting....')
            break

        case _:
            print('Invalid Choice!!')