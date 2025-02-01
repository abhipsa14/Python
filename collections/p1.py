#collection = single "variables" used to store multiple values
# List= [] ordered and changeable, Duplicates OK
# Set= {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple=() ordere and unchangeable. Duplicates OK. Faster

fruit =["apples","oranges","banana","coconut"] #list
print(fruit)

# print(dir(fruit))
# print(help(fruit))
print(len(fruit))
fruit.append("Guava")
print(fruit)
fruit.remove('apples')
# fruit.pop()
# del fruit
fruit.insert(0,'kiwi')
fruit.sort()
fruit.reverse()
print(fruit)
fruit.clear()
# for i in fruit:
#     print(i)
print(fruit)

## SET
fruits={"apple","orange","banana","coconut"}
# print(dir(fruits))
print(fruits)
# print(fruits[0]) #set is unordered and is not accessable
fruits.add("kiwi")
fruits.remove("apple")
fruits.pop()
print(fruits)

#TUPLES
# Methods are same as list itself
# index(),count()
fr=("apple","gauva","orange","kiwi","pineapple")
# print(dir(fr))
print(fr)
for x in fr:
    print(x,end=" ")
fr.count("kiwi")
