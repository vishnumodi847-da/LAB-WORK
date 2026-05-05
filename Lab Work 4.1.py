# Q1

# max
awe = ["m", "n", "b", "v"]
x = max(awe)
print(x)

# len
b = len(awe)
print(b)

# sorted
c = sorted(awe)
print(c)


# sum
amt = 12, 13, 55, 89, 78
s = sum(amt)
print(s)

# type()
name = "vishnu"
age = 20
height = 5.6
id = {25514}
school_name = ["ashadeep"]

print(type(name))
print(type(age))
print(type(height))
print(type(id))
print(type(school_name))


# Q2
def factorial(num):
    vis = 1
    for i in range(1, num + 1):
        vis = vis * i
    return vis


num = int(input("Enter number: "))
print(factorial(num))

# Q3


def square_list():
    num = input("Enter number: ")
    num = num.split(",")

    for i in num:
        v = int(i)
        print(v * v)


square_list()


# Q4
def feq():
    name = input("Enter your name: ")
    data = {}
    for i in name:
        if i in data:
            data[i] = data[i] + 1
        else:
            data[i] = 1
    print(data)


feq()


# Q5
def cube():
    num = input("Enter number: ")
    num = num.split(",")
    for i in num:
        n = int(i)
        print(n**3)


cube()

# Q6


def calc():
    num = input("Enter calc number: ")
    num = num.split(",")

    total = 0
    product = 1

    for i in num:
        i = int(i)
        total += i
        product *= i
    print("sum= ", total)
    print("product= ", product)


calc()

# Q7


def show_std(*nam):

    if len(nam) == 0:
        print("no student")
    else:
        for name in nam:
            print(name)


show_std("ram", "shiyam", "vijay")

# Q8


def alag(*vis):
    dd = []
    cc = []
    vv = []

    for i in vis:
        if type(i) == int:
            dd.append(i)
        elif type(i) == str:
            cc.append(i)
        else:
            vv.append(i)

    return {"age": tuple(dd), "name": tuple(cc), "other": tuple(vv)}


a = [2, 3, 5, 6, 8, 7, 25, 36, 4]

b = ["sanjay", "vishnu", "jay"]
c = [5.5, list]


print(alag(*a, *b, *c))

# Q9


def kwarg(**san):
    for key, value in san.items():
        print(key, ":", value)


kwarg(name="vishnu", age=20, city="surat")

# Q10


def total_cost(**pro):
    total = 0
    for i in pro:
        item = pro[i]

        name = item["name"]
        price = item["price"]
        quntity = item["quntity"]

        total += price * quntity
        print(name, "=", total)
    print("total cost", total)


total_cost(
    p1={"name": "vishnu", "price": 20, "quntity": 2},
    p2={"name": "jay", "price": 50, "quntity": 3},
)
