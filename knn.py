import math

# Calculate the Euclidean distance between two combos based on their odds
def euclidean_distance(combo1, combo2):
    odd1_diff = float(combo1['odd_1']) - float(combo2['odd_1'])
    odd2_diff = float(combo1['odd_2']) - float(combo2['odd_2'])
    #Apply Pythagorean theorem to calculate the distance
    distance = math.sqrt((odd1_diff ** 2) + (odd2_diff ** 2))
    return distance

#KNN algorithm:finds the k nearest combos and predicts the combo odds
def knn(data, new_combo, k=3):
    #Empty array to store distances
    distances = []
    #Calculate distance from new combo to every combo in the dataset
    for combo in data:
        distance = euclidean_distance(new_combo, combo)
        distances.append((distance, combo))
    #Sort by distance from smallest to largest
    distances.sort(key=lambda x: x[0])
    #Keep only the k nearest neighbors
    neighbors = distances[:k]
    total = 0
    for distance, combo in neighbors:
        total = total + float(combo['combo_odds'])
    #Calculate the average as our prediction
    prediction = total / k
    return prediction

#Read the CSV file and store all combos in an array
def combo_odds(filepath):
    results = []
    with open(filepath, 'r', encoding = "utf-8") as f:
        next(f)
        for line in f:
            columns = line.strip().split(',')
            combo = {"combo_label": columns[0],
                     "odd_1": columns[1],
                     "odd_2": columns[2],
                     "combo_odds": columns[3]}
            results.append(combo)
    return results

#Main function: runs the program
def main():
    filepath = input("Give the name of the file:").strip()
    data = combo_odds(filepath)
    print(f"Loaded {len(data)} combos")

    #Ask user for the new combo odds to predict
    new_combo = {"odd_1": input("Give odd_1: ").strip(), "odd_2": input("Give odd_2: ").strip()}
    prediction = knn(data, new_combo)
    print(f"Predicted combo odd: {prediction}")

main()
