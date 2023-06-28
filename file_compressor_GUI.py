import PySimpleGUI as sg

'''label1 = sg.Text("Enter feet: ")
input1 = sg.Input(tooltip = "Enter feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(tooltip = "Enter inches")

button = sg.Button("Convert")

window = sg.Window("Converter", layout = [[label1, input1], [label2, input2], [button]])
window.read()
window.close()'''

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input(tooltip = "Select files")
choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input(tooltip = "Select folder")
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",layout =  [[[label1],input1, choose_button1], [[label2], input2, choose_button2], [compress_button]],
                   font = ("Algerian", 10))
window.read()
window.close()
