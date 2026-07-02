import os
import sys

#Read a txt file and print all its contents at once
def read_txt(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        content = f.read()
    print(content)

def read_csv(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        #Read the entire file content at once
        content = f.read()
    print(content)

READERS = {".txt": read_txt, ".csv": read_csv}

#Main function: runs the program
def main():
    filepath = input("Give the name of the file: ").strip()
    #Check if the file exists
    if not os.path.exists(filepath):
        print ("File not found")
        sys.exit(1)

    #Get the file extension and convert to lowercase
    _,ext = os.path.splitext(filepath)
    ext = ext.lower()

    #Find the correct reader function for this file type
    reader = READERS.get(ext)
    #If file is not supported, stop the program
    if reader is None:
        print ("File not supported")
        sys.exit(1)

    print(f"File: {filepath}")
    print("=" * 30)
    #Call the appropriate reader function to display the file contents
    reader(filepath)

main()