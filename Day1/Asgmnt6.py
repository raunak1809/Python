Names=[]
Ages=[]
Emails=[]
for counter in range(0,3):
    name=input("enter the name")
    age=input("enter the age")
    email=input("enter the email")
    Names.insert(counter,name)
    Ages.insert(counter,age)
    Emails.insert(counter,email)

print(Names)
print(Ages)
print(Emails)