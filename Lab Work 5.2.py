# Q1


class person:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        print(self.name, "created")

    def __del__(self):
        print(self.name, "deleted")


f = person("vis", "21-10-2005")
del f


# Q2


class animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("ANIMAL NAME: ", self.name)


A1 = animal("Dog")
A2 = animal("Cat")
A1.display()
A2.display()

# Q3


class Rectangle:
    def __init__(self, length, width):
        self.lenth = length
        self.width = width

    def area(self):
        print("CALCULATED AREA: ", self.lenth * self.width)


are = Rectangle(12, 12)
are.area()


# Q4
class employee:
    def __init__(self):
        self.name = "VISHNU"
        self.salary = 2000000

    def display(self):
        print(f"{self.name} RECEIVED SALARY RS {self.salary}")

    def __del__(self):
        print("DELETED")


s1 = employee()
s1.display()
del s1


# Q5
class student:
    id = 1223

    def __init__(self, name, roll_num):
        self.name = name
        self.__roll_num = roll_num
        student.id += 1
        self.id = student.id

    def display(self):
        print(self.id, self.name, self.__roll_num)


f1 = student("JAY", 23)
f1.display()
