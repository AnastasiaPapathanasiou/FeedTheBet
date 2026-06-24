import os
import sys

#Read a txt file and print it line by line
def read_txt(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            print(line.strip())
            #Wait for user to press Enter before showing next line
            input()
#Read a csv file and print it line by line
def read_csv(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        for line in f:
            print(line.strip())
            input()
#Read a csv file and store all combos in an array
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

#Calculate the weighted average of two odds
#Default weights: 70% for odd_1 and 30% for odd_2
def weighted_average(odd_1, odd_2, weight_1=0.7, weight_2 = 0.3):
    #Multiply each odd by it's weight and sum them up
    result = (float(odd_1) * weight_1 + float(odd_2) * weight_2)
    return result

READERS = {".txt": read_txt, ".csv": read_csv}

#Main function: runs the program
def main():
    filepath = input("Give the name of the file: ").strip()
    #Check if the file exists
    if not os.path.exists(filepath):
        print ("File not found")
        sys.exit(1)

    #Get the file extension and conver to lowercase
    _,ext = os.path.splitext(filepath)
    ext = ext.lower()

    #Find th correct reader function for this file type
    reader = READERS.get(ext)
    #If file type is not supported, stop the program
    if reader is None:
        print ("File not supported")
        sys.exit(1)

    print(f"File: {filepath}")
    print("=" * 30)
    #Load all combos from the CSV
    data = combo_odds(filepath)
    print(f"Found {len(data)} combos")
    #Calculate and print weighted average for each combo
    for item in data:
        wa = weighted_average(item['odd_1'], item['odd_2'])
        print(f"Combo: {item['combo_label']} | Weighted Avg: {wa} | Combo Odds: {item['combo_odds']}")
main()
