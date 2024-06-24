contact={}

def display_contact():
    print("NAME\t\t(PHONE NUMBER , EMAIL , ADDRESS)")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        
while True:
    choice=int(input(" 1.Add contact\n 2.Search contact\n 3.Display contact\n"
                     +" 4.Update contact\n 5.Delete contatct\n 6.Exit\n"
                     +" Enter your choice:"))
    if choice==1:
        name=input("Enter name:")
        phone=int(input("Enter phone number:"))
        email=input("Enter email id:")
        address=input("Enter address:")
        contact[name]=phone,email,address
    elif choice==2:
        search_name=input("Enter name:")
        if search_name in contact:
            print(search_name,contact[search_name])
        else:
            print("contact not found")
    elif choice==3:
        if not contact:
            print("contact book is empty")
        else:
            display_contact()
    elif choice==4:
        update_contact=input("Enter name to be updated:")
        if update_contact in contact:
            phone=int(input("Enter phone number:"))
            email=input("Enter email id:")
            address=input("Enter address:")
            contact[update_contact]=phone,email,address
            print("contact updated")
            display_contact()
        else:
            print("Name not found in contact book")
    elif choice==5:
        del_contact=input("Enter name to be deleted:")
        if del_contact in contact:
            contact.pop(del_contact)
            display_contact()
        else:
            print("Name not found in contact book")
    elif choice==6:
        print("Exiting contact book")
        break
    else:
        break
