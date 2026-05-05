# Q1
with open("sample.txt", "w") as f:
    f.write("Python is a versatile programming langua")

# Q2
with open("sample.txt", "r") as f:
    print(f.read())

with open("sample.txt", "w") as f:
    f.write("Learning file handling in Python is fun!          #")

# Q3
with open("sample.txt", "r") as f:
    for line in f:
        print(line.rstrip("#"))

# Q4
with open("note.txt", "w") as f:
    f.write("Python is easy to learn.\n")
    f.write("It has numerous libraries.\n")
    f.write("File handling is one of its features.\n")

# Q5
with open("note.txt", "a") as f:
    f.write("Line 4: Python supports multiple modes of file handling.\n")
    f.write("mkj.\n")

# Q6
with open("note.txt", "rb") as f:
    data = f.read()
    print(data)

# Q7
with open("note.txt", "r") as f:
    g = f.read()

word = len(g.split())
char = len(g)
line = g.count("\n")

print(word)
print(char)
print(line)

# Q8
with open("sample.txt", "r+") as f:
    nu = f.read()
    print(nu)
    f.write("\nThis file was last modified by adding this sentence.")

# Q9
word = input("Enter your word for search  : ")
f = open("note.txt", "r")
lines = f.readlines()

h = 1

for i in lines:
    if word in i:
        print("Found in line ", h)
    h = h + 1
f.close()
