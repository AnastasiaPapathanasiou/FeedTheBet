import os
import sys

#Read a txt and print it line by line
def read_txt(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            #Print each line without extra whitespace
            print(line.strip())
            #Wait for user to press Enter before showing next line
            input()

#Read a csv file and print it line by line
def read_csv(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            print(line.strip())
            input()

#Read the csv file and print only the combo_odds value from each line
def combo_odds(filepath):
    with open (filepath, 'r', encoding = "utf-8") as f:
        #Skip the header line
        next (f)
        for line in f:
            columns = line.strip().split(',')
            #Get the 4th column which is the combo_odds
            combo_odds = columns[3]
            #Print only the combo_odds value
            print(combo_odds)

READERS = {".txt": read_txt, ".csv": read_csv}

#Main function: runs the program
def main():
    filepath = input("Give the name of the file: ").strip()
    if not os.path.exists(filepath):
        print ("File not found")
        sys.exit(1)

    _,ext = os.path.splitext(filepath)
    ext = ext.lower()

    reader = READERS.get(ext)

    #If file type is not supported, stop the program
    if reader is None:
        print ("File not supported")
        sys.exit(1)

    print(f"File: {filepath}")
    print("=" * 30)
    #Call combo_odds to print only the combo_odds values from the csv
    combo_odds(filepath)

main()
