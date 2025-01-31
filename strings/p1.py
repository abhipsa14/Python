#string methods

name=input("Enter name:")
phone_no=int(input("Enter your phone number:"))
res=len(name)

#res=name.find("i")
#res=name.rfind("p")#find the last ouccrence
#name=name.capitalize()
name=name.lower()
name=name.upper()
name=name.isalpha()
res=name.isdigit()
res=phone_no.count("-")
phone_no=phone_no.replace("-"," ")


print(name)

print(res)

help(str)
