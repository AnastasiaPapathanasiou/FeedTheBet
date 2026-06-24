import math

def euclidean_distance(combo1, combo2):
    odd1_diff = float(combo1['odd_1']) - float(combo2['odd_1'])
    odd2_diff = float(combo1['odd_2']) - float(combo2['odd_2'])
    distance = math.sqrt((odd1_diff ** 2) + (odd2_diff ** 2))
    return distance

def knn(data, new_combo, k=3):
    distances = []
    for combo in data:
        distance = euclidean_distance(new_combo, combo)
        distances.append((distance, combo))
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]
    total = 0
    for distance, combo in neighbors:
        total = total +float(combo['combo_odds'])
    prediction = total / k
    return prediction

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

def main():
    filepath = input("Give the name of the file:").strip()
    data = combo_odds(filepath)
    print(f"Loaded {len(data)} combos")

    new_combo = {"odd_1": input("Give odd_1: ").strip(), "odd_2": input("Give odd_2: ").strip()}
    prediction = knn(data, new_combo)
    print(f"Predicted combo odd: {prediction}")

main()
