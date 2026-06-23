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

def weighted_average(odd_1, odd_2, weight_1=0.7, weight_2 = 0.3):
    result = (float(odd_1) * weight_1 + float(odd_2) * weight_2)
    return result


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
        wa = weighted_average(item['odd_1'], item['odd_2'])
        print(f"Combo: {item['combo_label']} | Weighted Avg: {wa} | Combo Odds: {item['combo_odds']}")
main()
