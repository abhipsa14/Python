#validate user input exercise
#1. username is no more than 12 characters
#2.username numst not contain spaces
# 3.usrname must not contain digits

username=input("Enter a username:")
ct=username.count(" ")
if len(username)>12:
    print("YOur username cannot be more that 12 characters.")
elif(ct>0):
    print("It should not contain spaces.")
elif(username.isdigit()):
    print("Must not contain digits.")
else:
    print(f"Welcome {username}")