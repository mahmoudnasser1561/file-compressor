import FreeSimpleGUI as Sg

filesText = Sg.Text("Select files to compress:")
filesInput = Sg.Input()
fileChooseButton = Sg.FileBrowse("choose")

destinationText = Sg.Text("Select destination folder:")
destinationInput = Sg.Input()
destinationChooseButton = Sg.FolderBrowse()

compress_button = Sg.Button("File Compressor")

window = Sg.Window("File Compressor", layout=[
                                                [filesText, filesInput, fileChooseButton],
                                                [destinationText, destinationInput, destinationChooseButton],
                                                [compress_button]])

window.read()
window.close()