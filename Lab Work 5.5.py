# Q1
print("==================================\n Q1")

from abc import ABC, abstractmethod


class shape(ABC):

    @abstractmethod
    def area(self):
        pass


class circle(shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return 3.14 * self.a * self.a


class rectangle(shape):
    def __init__(self, c, b):
        self.c = c
        self.b = b

    def area(self):
        return self.c * self.b


bu = circle(20)
v=bu.area()
print(v)

vu = rectangle(21, 33)
w=vu.area()
print(w)


# Q2
print("==================================\n Q2")


from abc import ABC, abstractmethod


class shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class rectangle(shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a + self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class circle(shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return 3.14 * self.a * self.a

    def perimeter(self):
        return 2 * (3.14 * self.a)


f = rectangle(56, 12)
b = f.area()
n = f.perimeter()
print(b)
print(n)
d=circle(201)
c=d.area()
g=d.perimeter()
print(c)
print(g)

#Q3
print("==================================\n Q3")

from abc import ABC,abstractmethod
class MLModel(ABC):
    
    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class LinearRegressionModel(MLModel):
    def train(self):
        print("TRAIN DEPATED ON TIME")

    def predict(self):
        print("I AM PREDICT TRAIN WILL BE LATE AS PER HIS CURRENT TIME")

class DecisionTreeModel(MLModel):
    def train(self):
        print("TRAIN DECISION ON TREE MODEL")

    def predict(self):
        print("TRAIN PREDICT ON DECICION TREE MODEL")

h=LinearRegressionModel()
h.train()
h.predict()


# Q4
print("==================================\n Q4")
from abc import ABC, abstractmethod


# Encapsulation
class BankAccount:
    def __init__(self, acc_no, holder_name, balance):
        self.__acc_no = acc_no
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, holder_name, balance, interest_rate):
        super().__init__(acc_no, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest Added:", interest)


# Polymorphism
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        limit = self.get_balance() + 5000

        if amount <= limit:
            print("Withdrawn from Current Account:", amount)
        else:
            print("Overdraft Limit Exceeded")


# Abstraction
class Account(ABC):

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


# Testing
s = SavingsAccount(101, "Vishnu", 10000, 5)
s.deposit(2000)
s.withdraw(3000)
s.add_interest()
print("Final Balance =", s.get_balance())

print()

c = CurrentAccount(102, "Rahul", 8000)
c.withdraw(12000)
