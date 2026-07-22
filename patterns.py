# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print("")

#Right Angle Triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print("")

#Inverted Right Angle Triangle
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print("")

#Diamond Pattern
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print("",end=" ")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print("",end=" ")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()

#Armstrong Number
# n=int(input("Enter the number:"))
# sum=0
# temp=n
# while temp>0:
#     d=temp%10
#     sum+=d**3
#     temp=temp//10
# if n==sum:
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number") 

#Hollow Square Pattern
# n=int(input("Enter a number:"))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#Pascals Patterns
n=int(input())
for i in range(n):
    print(""*(n-i-1),end="")
    n=1
    for j in range(n-i-1):
        print("",end=" ")
    for j in range(i+1):
        print(n,end=" ")
        n=n*(i-j)//(j+1)
    print()