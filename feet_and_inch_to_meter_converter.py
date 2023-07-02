import PySimpleGUI as sg


from feet_inch_to_meter import feet_inch

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(tooltip = "Enter feet", key = "feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(tooltip = "Enter inches", key = "inches", size = (43,2))

output_label = sg.Text("Meters = ", text_color = "yellow")
output = sg.Text(key = "meter", text_color = "yellow")

button = sg.Button("Convert")

exit_button = sg.Button("Exit")

window = sg.Window("Converter", layout = [[label1, input1], [label2, input2], [output_label, output],[button, exit_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Convert":
            feet = values["feet"]
            inches = values["inches"]
            meters = feet_inch(feet, inches)
            window["meter"].update(value = str(meters) + " meters")

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()