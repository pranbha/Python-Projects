'''todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add" | "display":
            todo = input("Enter a todo: ")
            modified_todo = todo.capitalize()
            todos.append(modified_todo)
        case "show":
            for i in todos:
                print(i)
        case "exit":
            break
        case _:
            print("Entered wrong value")

print("Bye!")'''

'''country = input("Enter your country: ")
country = country.capitalize()

match country:
    case "USA":
        print("Hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")'''

'''todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add" | "display":
            todo = input("Enter a todo: ")
            modified_todo = todo.capitalize()
            todos.append(modified_todo)
        case "show":
            for index, i in enumerate(todos):
                print(f"{index + 1}. {i}")
        case "edit":
            number = int(input("Enter the number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter the number of todo that is completed: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Entered wrong value")

print("Bye!")'''

'''while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add" | "display":
            todo = input("Enter a todo: ") + "\n"
            todo = todo.capitalize()
            with open("todos.txt", "r") as f:
                todos = f.readlines()

            todos.append(todo)
            with open("todos.txt", "w") as f:
                f.writelines(todos)
        case "show":
            with open("todos.txt", "r") as f:
                todos = f.readlines()
                for index, i in enumerate(todos):
                    i = i.strip("\n")
                    print(f"{index + 1}. {i}")
        case "edit":
            number = int(input("Enter the number of todo to edit: "))
            number = number - 1

            with open("todos.txt", "r") as f:
                todos = f.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

            with open("todos.txt", "w") as f:
                f.writelines(todos)

        case "complete":
            number = int(input("Enter the number of todo that is completed: "))

            with open("todos.txt", "r") as f:
                todos = f.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as f:
                f.writelines(todos)

            print(f"Todo {todo_to_remove} was removed from the todo list")
        case "exit":
            break
        case _:
            print("Entered wrong value")

print("Bye!")'''

from todos_functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo.title()
        todos = get_todos()

        todos.append(todo + "\n")
        write_todos(todos)
    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = get_todos()
        for index, i in enumerate(todos):
            i = i.strip("\n")
            print(f"{index + 1}. {i}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.title() + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            print(f"Todo, {todo_to_remove} was removed from the todo list")

        except IndexError:
            print("There is no todo associated with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Entered wrong value")

print("Bye!")
