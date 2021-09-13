# -*- coding: utf-8 -*-

import pdf_extract
import PySimpleGUI as sg


##### SimpleGUI #####

# Upload button
#ul_button = [[sg.Text("Unfallbericht auswählen: "), sg.Input(), sg.FileBrowse()]]

layout = [[sg.T("")], [sg.Text("PDF auswählen: "), sg.Input(), sg.FileBrowse(key = "-FILE-")],[sg.Button("Submit")]]


# General Layout & Size
window = sg.Window(title="PDF Highlight Extractor", layout=layout, margins=(100, 100))#.read()


while True:
    event, values = window.read()
    #print(values["-FILE-"])
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit":
        file_name = values[r"-FILE-"].split("/")[-1]
        print(file_name)
        pdf_extract.main(file_name)
        window.close()
        