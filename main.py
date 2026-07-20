
#print("Mahesh\n"*3)
#print("\\tcurrent\\new\folder")
# \ is escape character
#print(r"\tcurrent\new\folder")

# def fun(n):
#    if n%2==0:
#        print("even")
#    elif n%2==1:
#         print("odd")
# n=int(input("Enter:"))
# fun(n)

# dict={
#     "name":"sriram",
#     "gender":"male",
#     "age":20,
#     "courses":["python","java"]
# }
# dict.update({"name":"Mahesh"})
# dict.update({"courses":"Python,Java,Machine Learning"})
# print(dict)
# def count(*args):
#     print(type(args))
# count(1,2,3,4,5)

# def dicts(**kwargs):
#     print(type(kwargs))
# dicts(name="Mahesh",Age=20,Gender="Male")
#OOPs
# x='Mahesh'
# x=x[1:-1]
# print(x[::-1])
# while True:
#     print("Hi")
# n=50
# sum=0
# while n>0:
#     sum+=n
#     n-=1
# print(sum)
n=50
sum=0
for i in range(1,n+1):
    sum+=n
    n-=1
print(sum)