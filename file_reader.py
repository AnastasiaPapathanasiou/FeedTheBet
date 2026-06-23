import os
import sys

def read_txt(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            print(line.strip())
            input()

def read_csv(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            print(line.strip())
            input()

READERS = {".txt": read_txt, ".csv": read_csv}

def main():
    filepath = input("Give the name of the file: ").strip()
    if not os.path.exists(filepath):
        print ("File not found")
        sys.exit(1)

    _,ext = os.path.splitext(filepath)
    ext = ext.lower()

    reader = READERS.get(ext)
    if reader is None:
        print ("File not supported")
        sys.exit(1)

    print(f"File: {filepath}")
    print("=" * 30)
    reader(filepath)

main()
