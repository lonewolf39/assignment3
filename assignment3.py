# Q.1- Create a list
l1=[]
a=int(input("Enter no. of integers"))
print(" Enter elements")
for i in range(a):
    x=int(input())
    l1.append(x)
print(l1)

# Q.2- Concatinate Lists
l2=['Dragon Ball','Hunter X Hunter','Fairy Tail']
l1.extend(l2)
print(l1)

# Q.3- Count the Occurance in a list
l3=[1,2,3,3,4,5,6,7,8,9,9,8]
print(l3.count(3))

# Q.4- Sort the List
l4=[10,11,1,5,44,5,8,39]
l4.sort()
print(l4)

#Q.5- Conctinate and sort 2 sorted arrays
l5=[2,3,5,64,56]
l6=[34,65,23,23,45]
print("sorted list: ",l5)
print("sorted list: ",l6)
l5.extend(l6)
print("merged: ",l5)
l5.sort()
print(l5)

#Q.6- Count Even and Odd numbers in a list
c1=0
c2=0
for i in l5:
    if(i%2==0):
        c1+=1
    else:
        c2+=1
print(c1)
print(c2)

#Q.7- Print a Tuple in reverse order
l7=[]
y=int(input("Enter Element"))
print("Enter integer")
for i in range(y):
    z=int(input())
    l7.append(z)
c3=tuple(l7)
print("tuple is:", c3)
r=reversed(c3)
print(tuple(r))

#Q.8- Find largest and smallest element of tuples
l8=[]
y=int(input("Enter Element"))
print("Enter integer")
for i in range(y):
    z=int(input())
    l8.append(z)
c3=tuple(l8)
print(max(c3),min(c3))

#Q.9- Convert a string to uppercase
s=(input("enter string\n"))
print(s.upper())

#Q.10- check if the string contains all numeric characters
s=(input("enter string\n"))
c=0
for i in range(len(s)):
    if s.isdigit():
        c=1;
    else:
        c=0;
        break;
if c==1:
    print("True")
else:
    print("False")

#Q.11- Replace the given string with your name
s=("Hello Sir")
print(s.replace("Hello Sir","Lonewolf"))
