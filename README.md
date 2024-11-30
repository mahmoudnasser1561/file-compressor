# File Compressor
A simple Python-based file compression tool that allows users to select files and compress them into a .zip archive. 
This tool uses PySimpleGUI for the graphical interface and Python's zipfile module for file compression

# Features

- **Select multiple files for compression**
- **Choose the destination folder for the compressed .zip file**
- **Simple and easy-to-use GUI built with PySimpleGUI**
- **Supports compression of various file types into a single .zip archive**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/file-compressor.git
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python compressor.py
   ```

## File Structure
```bash
file-compressor/
├── main.py           # Main entry point for the application
├── compress/         # Folder containing the compression logic
│   └── zip_creator.py  # Functionality to create zip archives
├── requirements.txt  # List of dependencies
└── README.md         # This file
```
