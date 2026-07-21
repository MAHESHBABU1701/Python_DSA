#4 Pillars of OOP's
#Encapsulation
#Access Modifiers
# class A:
#     def __init__(self,name,age,gender):
#         self.__name=name#private variable can be accessed inside of ame clas which defines with__
#         self._age=age #protected variable can be accessed inside of same class which defines with _
#         self.gender=gender#public variable can be accessed inside of same class and outside of the clas it defines without a sufix
#     def display(self):
#         print(self.__name)
#         print(self._age)
#         print(self.gender)
# a1=A("Mahesh", 20,"Male")
# a2=A("Vignesh", 21,"Male")
# print(a1.display())
# print(a2.display())

#Abstraction:
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdrawal(self,amount):
        self.__balance-=amount
    def getBalance(self):
        return self.__balance
    @abstractmethod
    def interestcalc(self):
        pass
class SavingAccount(BankAccount):
    def interestcalc(self):
        return self.balance*0.05

#Polymorphism:
class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")
