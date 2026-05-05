print("==================================\n Q1")


# Q1
class parent:
    def display(self):
        print("this is parent")


class child(parent):
    def show(self):
        print("this is child")


v = child()
v.display()
v.show()
print("==================================\n Q2")

# Q2


class teacher:
    def work(self):
        print("teacher work is done")


class administrator:
    def admini(self):
        print("addmission of student")


class headmaster(teacher, administrator):
    def headmini_work(self):
        print("check work of teacher and administrator")


mn = headmaster()
mn.work()
mn.admini()
mn.headmini_work()
print("==================================\n Q3")

# Q3


class grandfather:
    def grand(self):
        print("GRANDFATHER NAME : ", "VIJAY")


class parent(grandfather):
    def par(self):
        print("PARENT NAME : ", "RAMESH")


class child(parent):
    def chil(self):
        print("CHILD NAME : ", "KUSH")


q = child()
q.grand()
q.par()
q.chil()
print("==================================\n Q4")

# Q4


class animal:
    def sound(self):
        print("animal make sound")


class dog(animal):
    def voice(self):
        print("dog sound is woof woof")


class cat(animal):
    def meow(self):
        print("cat sound is meow")

d = dog()
d.sound()
d.voice()
print("==================")
c = cat()
c.sound()
c.meow()

print("==================================\n Q5")

# Q5


class grandparents:
    def __init__(self):
        self.name = "RAHUL"


class parent_1(grandparents):
    def __init__(self):
        super().__init__()
        self.parent1 = "VIRAT"


class parent_2(grandparents):
    def __init__(self):
        super().__init__()
        self.parent2 = "DHONI"


class child(parent_1, parent_2):
    def __init__(self):
        super().__init__()
        self.child1 = "AKAY"


s = child()
print("GRANDPARENT NAME: ", s.name)
print("PARENT 1 NAME: ", s.parent1)
print("PARENT 2 NAME: ", s.parent2)
print("CHILD NAME: ", s.child1)


print("==================================\n Q6")

# Q6

a = 12
b = "name"
c = 2.3
v = ["modi"]

print(type(a))
print(type(b))
print(type(c))
print(type(v))
print("==================================\n Q7")


# Q7
class student:
    name = "Vishnu"

    def display(self):
        print("Student class")


obj = student()

print(dir(obj))


print("==================================\n Q8")

# Q8


class animal:
    pass


class dog(animal):
    pass


class cat(animal):
    pass


d = dog()
c = cat()
a = animal()
print(isinstance(d, dog))
print(isinstance(dog, animal))
print(isinstance(c, cat))
print(isinstance(a, animal))


print("==================================\n Q9")
# Q9

help(print)

class person:
    def __int__(self,name):
        self.name=name

help(person)
help(person.__init__)