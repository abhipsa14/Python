n=int(input("Enter number of numbers in a list:"))
lst=[]
for i in range(n):
    i = int(input("Enter a number:"))
    lst.append(i)

for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(lst[j]>lst[j+1]):
            c=lst[j+1]
            lst[j+1]=lst[j]
            lst[j]=c
        
    
print(lst)
