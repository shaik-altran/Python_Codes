import xlrd


path=r'/home/shaik/Documents/Copy of my_sheet.xls'
excel_workbook = xlrd.open_workbook(path)
excel_sheet = excel_workbook.sheet_by_index(0)


def CopyExceltodict():
    for column in range(1,excel_sheet.ncols):
        for row in range(excel_sheet.nrows):
            contactinDictionary.update({excel_sheet.cell_value(row,0) :  excel_sheet.cell_value(row,column)})
            if row == excel_sheet.nrows-1:
                ListofDictionaries.append(contactinDictionary.copy())

# ABOVE FUNCTION WILL COPY DATA IN EXCEL TO THE LIST OF DICTIONARIES


class Contacts:

    def Searchforcontacts(self,name):
        self.name = name
        nameexist = 0
        print('\n')
        for contact in ListofDictionaries :
            for infoincontact in contact:
                if name in str(contact[infoincontact]):
                    nameexist += 1
                    print(contact)
                    break

        if nameexist == 0:
            print("Looks like {0} is not saved in phonebook".format(name))

# ABOVE FUNCTION WILL SEARCH FOR EXISTING CONTACTS


    def Viewallcontacts(self):
        for contact in ListofDictionaries:
            print('\n')
            print(contact)

# ABOVE FUNCTION WILL VIEW EVERY CONTACT IN LIST 


    def Deleteallcontacts(self):
        while(1):
            print("Are you sure you want to delete all the contacts??")
            print("1.Yes 2.No")
            select = int(input("Enter your choice: "))
            if select == 1:
                ListofDictionaries.clear()
                print("deleted... your phonebook is empty")
                print(ListofDictionaries)
                exit()
            elif select == 2:
                return
            else:
                print("select the correct choice!!")

# ABOVE FUNCTION WILL DELETE EVERY CONTACT IN LIST


    def Editcontact(self,existingname,replacingname):
        self.existingname = existingname
        self.replacingname = replacingname
        contactid = 0
        count = 0
        nameexist = 0
        for contact in ListofDictionaries:
            contactid += 1
            for infoincontact in contact:
                if existingname == contact[infoincontact]:
                    nameexist += 1
                    print("\nContact_id = {0}".format(contactid))
                    print(contact)
        if nameexist == 0:
            print("\nLooks like {0} is not saved in phonebook".format(existingname))
            return
        contactid = int(input("\nAbove mentioned contacts with their id's please select the id which you want to edit: "))
        for contact in ListofDictionaries:
            count += 1
            for infoincontact in contact:
                if count == contactid:
                    if existingname == contact[infoincontact]:
                        contact[infoincontact] = replacingname
                        print("\nyour contact info with {0} is replaced with {1}\n".format(existingname,replacingname))
                        print(contact)
                        break

# ABOVE FUNCTION WILL EDIT PARTICULAR SELECTED CONTACT
    def Contacttodelete(self,contacttodelete):
        self.contacttodelete = contacttodelete
        contactid = 0
        count = 0
        nameexist = 0
        for contact in ListofDictionaries:
            contactid += 1
            for infoincontact in contact:
                if contacttodelete == contact[infoincontact]:
                    nameexist += 1
                    print("\nContact_id = {0}".format(contactid))
                    print(contact)
        if nameexist == 0:
            print("\nLooks like {0} is not saved in phonebook".format(contacttodelete))
            return
        contactid = int(input("\nAbove mentioned contacts with their id's please select the id which you want to delete: "))
        for contact in ListofDictionaries:
            count += 1
            for infoincontact in contact:
                if count == contactid:
                    if contacttodelete == contact[infoincontact]:
                        choice = int(input("Are you sure you want to delete '{0}' select 1 for Yes or 2 for No : ".format(contacttodelete)))
                        if choice == 1:
                            contact.clear()
                            print("\n your contact {0} is deleted succesfully\n".format(contacttodelete))
                            print(ListofDictionaries)
                            break
                        elif choice == 2:
                            return
                        else:
                            print("wrong choice selected\n")

# ABOVE FUNCTION WILL DELETE THE PARTICULAR SELECTED CONTACT


contactinDictionary = {}
ListofDictionaries = []


CopyExceltodict()

Phonebook = Contacts()


while 1:
        print("********PHONEBOOK*********")
        print("1. Searching for a Peron??")
        print("2. view all contacts")
        print("3. Delete all contacts")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            Person = input("Enter the person you want to search: ")
            Phonebook.Searchforcontacts(Person)
            print('\n')

        elif choice == 2:
            Phonebook.Viewallcontacts()
            print('\n')


        elif choice == 3:
            Phonebook.Deleteallcontacts()

        elif choice == 4:
            existingname = input("Enter existing information of contact: ")
            replacingname = input("Enter the information to be replaced: ")
            Phonebook.Editcontact(existingname,replacingname)
            print('\n')


        elif choice == 5:
            contacttodelete = input("Enter the contact name you want to delete: ")
            Phonebook.Contacttodelete(contacttodelete)
            print('\n')


        elif choice == 6:
            print("\nGood Bye..\n")
            break
        else:
            print("\nWorng choice selected!!!\n")

