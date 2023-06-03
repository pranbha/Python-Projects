import todos_functions

import PySimpleGUI as sg

label = sg.Text("Type a To-Do")
input_box = sg.InputText(tooltip = "Enter To-Do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label],[input_box, add_button]])
window.read()
window.close()