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

def combo_odds(filepath):
    results = []
    with open (filepath, 'r', encoding = "utf-8") as f:
        next(f)
        for line in f:
            columns = line.strip().split(',')
            combo = {"combo_label": columns[0],
                     "odd_1": columns[1],
                     "odd_2": columns[2],
                     "combo_odds": columns[3]}
            results.append(combo)
    return results

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
    data = combo_odds(filepath)
    print(f"Found {len(data)} combos")
    for item in data:
        print(item)

main()
