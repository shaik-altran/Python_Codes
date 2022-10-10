class contact:
    __FirstName = ''
    __LastName  = ''
    __PhoneNo = ''
    __Email_id = ''
    def __init__(self,Fn,Ln,Phno,Email):
        self.__FirstName = Fn
        self.__LastName  = Ln
        self.__phoneNo   = Phno
        self.__Email_id  = Email

class Phonebook:
    __ListofObjects = []
    __ObjectinList  = []
    def AddContact(self):
        Fn       = input("Enter First Name: ")
        Ln       = input("Enter Last Name: ")
        phno     = input("Enter Phone Number: ")
        Email    = input("Enter Email_id: ")
        
        Object   = contact(Fn,Ln,phno,Email)
        
        self.__ObjectinList.insert(0, Object._contact__FirstName)
        self.__ObjectinList.insert(1, Object._contact__LastName)
        self.__ObjectinList.insert(2, Object._contact__phoneNo)
        self.__ObjectinList.insert(3, Object._contact__Email_id)
        
        self.__ListofObjects.append(self.__ObjectinList.copy())
        self.__ObjectinList.clear()
        print(self.__ListofObjects)

    def DisplayContacts(self):
        print(self.__ListofObjects)

    def DeleteContact(self):
        ContacttoDelete = input("Enter the Contact to delete: ")
        nameexist = 0
        for contact in self.__ListofObjects:
            for infoincontact in contact:
                if ContacttoDelete == infoincontact:
                    nameexist += 1
                    contact.clear()
                    break
        if nameexist == 0:
            print("Looks like {0} is not saved in phonebook".format(ContacttoDelete))

    def SearchforContact(self):
        Name = input("Enter the Name of Contact: ")
        nameexist = 0
        for contact in self.__ListofObjects :
            for infoincontact in contact:
                if Name in infoincontact:
                    nameexist += 1
                    print(contact)
                    break
        
        if nameexist == 0:
            print("Looks like {0} is not saved in phonebook".format(Name))


FirstPhonebook = Phonebook()

while True:
    print("1.Add Contact")
    print("2.Display Contacts")
    print("3.Search For Contacts")
    print("4.Delete Contact")
    print("5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        FirstPhonebook.AddContact()
    elif choice == 2:
        FirstPhonebook.DisplayContacts()
    elif choice == 3:
        FirstPhonebook.SearchforContact()
    
    elif choice == 4:
        FirstPhonebook.DeleteContact()
    elif choice == 5:
        break
        
    else:
        print("Wrong Choice Selected")

