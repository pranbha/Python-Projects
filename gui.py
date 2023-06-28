import todos_functions

import PySimpleGUI as sg

label = sg.Text("Type a To-Do")
input_box = sg.InputText(tooltip = "Enter To-Do", key = "todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box], [add_button, exit_button]],
                   font = ("Helvetica", 10))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = todos_functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo.title())
            todos_functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()