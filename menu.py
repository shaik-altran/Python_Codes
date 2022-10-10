def my_menu():
    while 1:
        print("********PHONEBOOK*********")
        print("1. Searching for a Peron??")    
        print("2. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            input("Enter the name of the person: ")
            print("okay he is there")
        elif choice==2:
            exit()
        else:
            print("Oh! Ohh!! Cannot find the Person")
