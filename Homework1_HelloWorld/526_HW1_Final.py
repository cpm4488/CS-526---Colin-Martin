import os 
from docx import Document

print("This script will read any .txt or .docx files")
print("If file is not located in a searched folder, paste the file location as a path.")
print("Searched Locations:")
print(" - Desktop")
print(" - Downloads")
print(" - Documents")
print(" - Same folder where this python script is saved")
print("")
filename = input("Enter the name of the .txt or .docx file: ").strip().strip('"').strip("'")
filename = filename.replace("\\ ", " ")

possible_names = [filename]
if not filename.lower().endswith((".txt", ".docx")):
    possible_names = [filename + ".txt", filename + ".docx"]

filepath = None
for path in possible_names:
    if os.path.isfile(path):
        filepath = path
        break
if filepath is None:
    name_only = os.path.basename(filename)
    possible_names = [name_only]
    if not name_only.lower().endswith((".txt", ".docx")):
        possible_names = [name_only + ".txt", name_only + ".docx"]

home = os.path.expanduser("~")
folders = [
    os.getcwd(),
    os.path.join(home, "Desktop"),
    os.path.join(home, "Downloads"),
    os.path.join(home, "Documents"),
]

for root_folder in folders:
    for current_folder, subfolders, files in os.walk(root_folder):
        for name in possible_names:
            if name in files:
                filepath = os.path.join(current_folder, name)
                break
        if filepath:
            break
    if filepath:
        break

if filepath is None:
    print("Error: file not found in current folder, Desktop, Downloads, or Documents.")
else:
    try:
        if filepath.lower().endswith(".docx"):
            doc = Document(filepath)
            for paragraph in doc.paragraphs:
                print(paragraph.text)
        else:
            f = open(filepath)
            for line in f:
                print(line.rstrip("\n"))
            f.close()
    except UnicodeDecodeError:
        print("Error: make sure this file is saved as a .txt or .docx")
