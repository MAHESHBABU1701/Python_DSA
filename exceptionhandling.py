# errors
# Value Errors-data type error
# Type KeyError-operations on incompatible types
# Index Error- Index out of range
# Key Erro-Key is not present
# Name Error-
# x=int(input("enter the number:"))
# y=int(input("enter the number:"))
# print(x/y)
# x=int(input("enter the number:"))
# y=int(input("enter the number:"))
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print("done")
# for i in range(5):
#     print(i)
# else:
#     print("done")
# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else:
#     print("done")

# try:
#     a=input("enter a name:")
#     print(a)
# except ValueError as e:
#     print(e)
# else:
#     print("done")

# a=int(input("enter a number"))
# if a<0:
#     raise ValueError("Number is negative")
# else:
#     print(a)

#TASK 2
# try:
#     l=[1,2,3,4,5,6,7,8,9,10]
#     print(l[11])
# except IndexError as i:
#     print(i)
# finally:
#     print("done")

#TASK 1
# while True:
#     try:
#         a = int(input("Enter a number: "))
#         print(a)
#         break
#     except ValueError as e:
#         print(e)
#     finally:
#         print("Done")
