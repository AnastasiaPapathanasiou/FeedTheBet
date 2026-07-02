import os
import sys

#Read a txt file and print it line by line
def read_txt(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            print(line.strip())
            input()

#Read a csv file and print it line by line
def read_csv(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            print(line.strip())
            input()

#Read the csv file and store all combos in an array as dictionaries
def combo_odds(filepath):
    #Empty array to store the combos
    results = []
    with open (filepath, 'r', encoding = "utf-8") as f:
        next(f)
        for line in f:
            #Store each combo as a dictionary with its 4 values
            columns = line.strip().split(',')
            combo = {"combo_label": columns[0],
                     "odd_1": columns[1],
                     "odd_2": columns[2],
                     "combo_odds": columns[3]}
            #Add combo to results array
            results.append(combo)
    #Return the full array of combos
    return results

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
    if reader is None:
        print ("File not supported")
        sys.exit(1)

    print(f"File: {filepath}")
    print("=" * 30)
    #Load all combos from the csv into an array
    data = combo_odds(filepath)
    #Print how many combos were found
    print(f"Found {len(data)} combos")
    for item in data:
        print(item)

main()
