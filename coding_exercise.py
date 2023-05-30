'''ranking = ['John', 'Sen', 'Lisa']

name = input("Enter the name: ")
name = name.capitalize()

rank = ranking.index(name) + 1
print(rank)'''


'''a = ["document", "presentation", "powerpoint"]

for index, i in enumerate(a):
    print(f"{index + 1}. {i.capitalize()}.txt")'''

'''contents = ["File 1 content.", "File 2 content", "File 3 content"]
filenames = ["file1.txt", "file2.txt", "file3.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)'''

'''file = open("essay.txt", "r")
print(file.read())
file.close()

with open("essay.txt", "r") as f:
print(len(file.read()))'''

'''member = input("Enter the name of the new member: ")

with open("members.txt", "r") as f:
    existing_members = f.readlines()

existing_members.append(member + "\n")

with open("members.txt", "w") as f:
    f.writelines(existing_members)'''

'''filenames = ["text_file_1.txt", "text_file_2.txt", "text_file_3"]

for filename in filenames:
    with open(filename, "w") as f:
        f.write("Hello")'''

'''filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    with open(filename, "r") as f:
        print(f.read())'''

'''c = 0
u = 0
password = input("Enter new password: ")

if len(password) >= 8:
    for i in password:
        if i.isdigit():
            c = c+1
    if c >= 2:
        for i in password:
            if i.isupper():
                u = u + 1
        if u >= 3:
            print("Strong password")
        else :
            print("Type atleast 3 words")
    else:
        print("Type atleast 2 digits")
else:
    print("Weak password")'''

'''def average():
    with open("todos.txt", "r") as f:
        data = f.readlines()

    l1 = []
    for i in data:
        l1.append(int(i))

    average1 = sum(l1)/len(l1)
    return average1


avg = average()
print(avg)'''



