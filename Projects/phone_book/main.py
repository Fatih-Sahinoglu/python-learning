from pbclass import PhoneBook #from file import class
pb=PhoneBook()


while True:
    print("\nPhone Book")
    print("1.Add Contact")
    print("2.List Contact")
    print("3.Delete Contact")
    print("4.Exit")

    choice=int(input("Please Enter Your Choice: "))

    if choice==1:
        name=input("Please write name: ")
        surname=input("Please write surname: ")
        number=int(input("Please write number: "))
        pb.add(name,surname,number)

    elif choice==2:
        pb.show()

    elif choice==3:
        name=input("Please enter name to delete: ")
        pb.delete(name)

    elif choice==4:
        print("Exiting...")
        break
    
    else:
        print("Wrong Value")

print("Goodbye")