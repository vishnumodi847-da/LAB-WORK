print("==================================\n Q1")


# Q1
def add(v, m):
    return v + m


print(add(100, 200))
print(add("hello", "world"))

# Q2
print("==================================\n Q2")


class sharpe:
    def area(self):
        pass


class circle(sharpe):
    def area(self):
        r = 5
        print(3.14 * r, r)


class rectangel(sharpe):
    def area(self):
        l = 10
        w = 20
        print(l * w)


c = circle()
r = rectangel()

c.area()
r.area()

# Q3
print("==================================\n Q3")

name = "vishnu modi"
number = [10, 20, 30]
dic = {"name": "visg", "date": 21}

print(len(name))
print(len(number))
print(len(dic))


# Q4
print("==================================\n Q4")


class transport:
    def travel(self):
        print("TRAVEL TICKET BOOKED")


class train(transport):
    def travel(self):
        print("TRAIN TICKET BOOKED FOR GOA")


class plan(transport):
    def travel(self):
        print("PLAN TICKET BOOK FOR THAILAND")


Rail = train()
Air = plan()

Rail.travel()
Air.travel()


# Q5
print("==================================\n Q5")


class calculator:
    def multiply(self, a, b, c=2):
        print("multiply", a * b * c)


obj = calculator()
obj.multiply(12, 12, 1)


# Q6
print("==================================\n Q6")


class animal:
    def speak(self):
        print("ANIMAL VOICE")


class dog(animal):
    def speak(self):
        print("DOG VOICE IS WOOF WOOF")


class cat(animal):
    def speak(self):
        print("CAT VOICE IS MEOW")


delta = dog()
alfa = cat()
delta.speak()
alfa.speak()


# Q7
print("==================================\n Q7")


class shape:
    @staticmethod
    def area(a, b=None):
        if b is None:
            print("CIRCLE: ", 3.14 * a * a)
        else:
            print("RECTANGEL: ", a * b)


shape.area(5)
shape.area(10, 20)


# Q8
print("==================================\n Q8")


class vehical:
    def start(self):
        print("VEHICAL FUAL TYPE.")


class bike(vehical):
    def start(self):
        print("BIKE FUAL TYPE IS PETROL.")


class car(vehical):
    def start(self):
        print("CAR FUAL TYPE IS DIESAL.")


hero = bike()
maruti = car()

hero.start()
maruti.start()

# Q9
print("==================================\n Q9")


class printer:
    def print(self, a=None, b=None):
        if a is not None and b is None:
            print("SINGLE VALUE: ", a)
        elif a is not None and b is not None:
            print("TWO VALUE: ", a, b)
        else:
            print("RETRY")


data = printer()
data.print("hii")
data.print(1200, 3200)

# Q10
print("==================================\n Q10")


class person:
    pass


class students(person):
    pass


print(issubclass(students, person))

# Q11
print("==================================\n Q11")


class employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class manager(employee):
    def __init__(self, name, number, salary):
        super().__init__(name, salary)
        self.salary = salary

    def display(self):
        print(self.name, self.number, self.salary)


data = manager("HARDIK", 322566453, 100000)
data.display()

# Q12
print("==================================\n Q12")


class grandparents:
    pass


class parents(grandparents):
    pass


class child(parents):
    pass


print(issubclass(grandparents, child))
print(issubclass(parents, child))
print(issubclass(parents, grandparents))
print(issubclass(child, grandparents))

# Q13
print("==================================\n Q13")


class base:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class derived(base):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def display(self):
        print(self.a, self.b, self.c)


hui = derived("vishnu:", "21-10-2005:", 6359547615)
hui.display()


# Q14
print("==================================\n Q14")


class user:
    def display(self):
        print("USER ADD SUCCESSFULLY")


class admin(user):
    def display(self):
        super().display()
        print("ADMIN DATA SHOW")


asd = admin()
asd.display()
