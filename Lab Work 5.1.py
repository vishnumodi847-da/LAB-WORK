# # Q1
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)


# P1 = person(["VISHNU"], [20])
# P2 = person(["RIDDHI"], [20])

# P1.display()
# P2.display()

# Q4


class book:
    def __init__(self):
        self.__title = None
        self.__author = None

    def set_data(self, title, author):
        self.__title = title
        self.__author = author

    def get_data(self):
        print(f"{self.__title} book is developed by {self.__author}")


b1 = book()
b1.set_data("python", "vishnu")
b1.get_data()

# Q2


class count:
    name = "vishnu"
    name_id = 0

    def __init__(self, name):
        self.name = name
        count.name_id += 1
        self.name_id = count.name_id

    def display(self):
        print(self.name_id, self.name)


counter1 = count("vishnu")
counter2 = count("kisu")

counter1.display()
counter2.display()


# Q5
class bank:
    def __init__(self, cust_name, acc_number, balance):
        self.cust_name = cust_name
        self.__acc_number = acc_number
        self.__balance = balance

    def display(self):
        print(self.cust_name, self.__acc_number, self.__balance)

    def check_balance(self):
        print(self.__balance)

    def deposit(self, val):
        self.__balance += val

    def withdraw(self, val):
        if val > self.__balance:
            print("insufficiant balance")
        else:
            self.__balance -= val
            print("balance added")


a = bank("vishnu", 233356, 8000)
a.display()
a.deposit(20)
a.check_balance()
a.withdraw(1000)
a.check_balance()
# Q6


class person:
    def __init__(self):
        self.__per_age = 0

    def set_age(self, per_age):
        if per_age > 0:
            self.__per_age = per_age
            print("SUCCESSFULLY UPDATE")
        else:
            print("invaild capture")

    def get_age(self):
        return self.__per_age


p = person()
p.set_age(20)
print(p.get_age())

# Q7


class student:

    def __init__(self, name, m1, m2, m3,avg=0):
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.avg=avg
    @property
    def display(self):
        self.avg = (self.__m1 + self.__m2 + self.__m3 / 3)
        print(self.__name)
        print(" ==================== \n   NAME DISPLAY DONE   \n ====================")
        print(self.avg)
        print(" ==================== \n    AVG DISPLAY DONE \n ====================")
    
    def grade(self):
        if self.avg >= 90:
            print("A")
        elif self.avg >= 80:
            print("B+")
        elif self.avg >= 60:
            print("C")
        else:
            print("D")
        print(" ==================== \n  GRADE DISPLAY DONE \n ====================")


c = student("vishnu", 210, 230, 111)
c.display
c.grade()
