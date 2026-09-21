526 HW Instructions - 

Part 1 - Introduction 
File is located in this folder named "HW1 - Introduction"


Part 2 - Hello World Coding Assignment

Implementation:

Check whether the input file is a .txt or a .docx by looking at the extension and read them based on the file type. The script will read .txt files as plain text and will use the docx library to read the .docx files.

Search most common folders and subfolders (Desktop, Documents, and Downloads) by default to only require a file path as the input if it is not found within any of these folders or wherever the .py file is stored. The pasted file path also would need to replace elements unique to Windows or Mac to make it readable in the search. 

Error messages will be printed if unsupported file types are used or if a file isn't found.

Execution Notes- 
- This script search for and read any .docx or .txt file located within a subfolder or directly inside the Desktop, Documents, Downloads, or the folder which 526_HW1_Final.py is saved. 
- If the file is saved in another folder, copy the file as a path and paste it into the input section that opens in the command prompt after running the file.
- Document extensions (.txt, .docx) are not required in the file input.

Execution Steps:
	1) Download the 526_HW1_Final.py locally to your laptop.
	2) Ensure that python is installed and connected to the software you'll be running the script on
	3) In your systems terminal line, run one of the following scripts to install the docx package
		- "python3 -m pip install python-docx"
		- "python -m pip install python-docx"
	If you receive a "externally managed environment" error, add --break-system-packages to the end of the command and run it again.
	4) Run the python script in the command or terminal window (.../526_HW1_Final.py)
		- If pasting the .py file does not work because of a permissions error, add python3 before the filename
	5) Enter the desired .txt or .docx file name into the command prompt
	6) Upon execution, you'll be able to enter the desired file name and after clicking enter, the text will appear on the command line.
