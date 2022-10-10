class contact:
    FirstName = ''
    LastName  = ''        
    PhoneNo = ''
    Email_id = ''
    def __init__(self,Fn,Ln,Phno,Email):
        self.FirstName = Fn
        self.LastName  = Ln
        self.phoneNo   = Phno
        self.Email_id  = Email
    def viewContact(self):
        thisdict = {}
        thisdict.update({"FirstName" : self.FirstName})
        thisdict.update({"LastName"  : self.LastName})
        thisdict.update({"Phno"      : self.phoneNo})
        thisdict.update({"Email_id"  : self.Email_id})
        print(thisdict)

contact1 = contact('shaik','Fairoz',8790696553,'shaik@gmail.com')
print(contact1.viewContact())






