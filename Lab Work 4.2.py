# Q6


# Create a lambda function to calculate the square of a number.
# Use it inside map() to generate list of squares.

sequre = [20, 30, 50]

abc = lambda x: x**2

sequre_list = list(map(abc, sequre))

print("original number:", sequre)

print("sequre number", sequre_list)

# Q7

# Filter out odd numbers using lambda and filter()

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
number_list = list(filter(lambda x: x % 2 == 0, number))

print("number:", number)

print("even number: ", number_list)

# Q8

# Lambda that accepts three numbers and returns the largest..

largest = lambda a, b, c: max(a, b, c)

print("largest number 10,20,01:", largest(10, 20, 1))


# Q9

# Program using global variable to count function calls

count = 0


def mycount():
    global count
    count += 1
    print(f"hello this function print {count} times")


mycount()
mycount()
print(f"total calls:{count}")

# Q10
# Global variable to keep track of sum of all numbers entered by user
total = 0


def add():
    global total
    num = input("number: ")
    nums = num.split(",")
    for i in nums:
        total += int(i)


add()
print(total)

# Q11
# Modify global variable (username) using a function

Username = "vishnu"


def update_username():
    global Username
    name = str(input("Enter Name: "))
    if name:
        Username = name
        print(f"Username Updated to :", {name})
    else:
        print("Not update")


update_username()
print(Username)
