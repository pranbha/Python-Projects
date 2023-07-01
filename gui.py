import todos_functions

import PySimpleGUI as sg

label = sg.Text("Type a To-Do")
input_box = sg.InputText(tooltip = "Enter To-Do", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = todos_functions.get_todos(), key = "todos", enable_events = True, size = (45, 10), tooltip = "List of Todos")
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box, add_button], [list_box], [edit_button, exit_button]],
                   font = ("Helvetica", 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = todos_functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo.title())
            todos_functions.write_todos(todos)
            window["todos"].update(values = todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = todos_functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            todos_functions.write_todos(todos)
            window["todos"].update(values = todos)

        case "todos":
            window["todo"].update(value = values["todos"][0])

        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()