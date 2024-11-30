import PySimpleGUI as Sg
from zip_creator import make_archive

filesText = Sg.Text("Select files to compress:")
filesInput = Sg.Input()
fileChooseButton = Sg.FileBrowse("Choose Files", key="ChooseFiles")

destinationText = Sg.Text("Select destination folder:")
destinationInput = Sg.Input()
destinationChooseButton = Sg.FolderBrowse()

compress_button = Sg.Button("File Compressor")

# Layout for the window
layout = [
    [filesText, filesInput, fileChooseButton],
    [destinationText, destinationInput, destinationChooseButton],
    [compress_button]
]

# Create the window
window = Sg.Window("File Compressor", layout=layout)

# Event loop
while True:
    event, values = window.read()
    if event == Sg.WINDOW_CLOSED:
        break
    elif event == "ChooseFiles":
        file_paths = values["files"].split(";")
        folder = values["folder"]
        make_archive(file_paths, folder)
        if file_paths:
            filesInput.update(file_paths)
    elif event == "File Compressor":
        # Add your compression logic here
        print("Selected files:", values[0])
        print("Destination folder:", values[1])

window.close()
