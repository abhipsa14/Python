#dictionary: a collection of  {key:value} pairs
#  ordered and changeable. No duplicate key allowed


capitals={"UP":"Lucknow","MP":"Bhopal","Assam":"Dispur","Maharashtra":"Mumbai"}

#print(dir(capitals))
#print(help(capitals))
print(capitals.get("Assam"))
print(capitals.get("Japan"))# will return None

#pop()
capitals.pop("UP")
#popitem()
capitals.popitem()#pops out the last element
#update
capitals.update({"MP":"jk"})

#keys()-->returns the keys of the dictionary

#values()--->returns the values of the dictionary


#items()--->it represents each key:value pair as a tuple and returns it
for key,value in capitals.items():
    print(f"{key}:{value}")