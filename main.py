import PySimpleGUI as Sg
from compress.zip_creator import make_archive

filesText = Sg.Text("Select files to compress:")
filesInput = Sg.Input(key="files")  # Correct key for the file input
fileChooseButton = Sg.FileBrowse("Choose Files", key="ChooseFiles")

destinationText = Sg.Text("Select destination folder:")
destinationInput = Sg.Input(key="folder")
destinationChooseButton = Sg.FolderBrowse()

compress_button = Sg.Button("File Compressor")
output = Sg.Text("", size=(40, 1), key="output")

layout = [
    [filesText, filesInput, fileChooseButton],
    [destinationText, destinationInput, destinationChooseButton],
    [compress_button],
    [output]
]

# Create the window
window = Sg.Window("File Compressor", layout=layout)

# Event loop
while True:
    event, values = window.read()

    if event == Sg.WINDOW_CLOSED:
        break

    if event == "File Compressor":
        filepaths = values["files"].split(";")
        folder = values["folder"]

        if filepaths and folder:
            make_archive(filepaths, folder)

            window["output"].update("Compression Completed!")
        else:
            window["output"].update("Please select both files and destination folder.")

window.close()
