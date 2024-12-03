with open("data.txt") as file:
    data = file.read().split("\n")
    col1 = [line.split("   ")[0] for line in data]
    col2 = [line.split("   ")[1] for line in data]
    
    col1 = sorted(col1)
    col2 = sorted(col2)

    distance = 0
    similarity = 0
    for i, _ in enumerate(col1):
        distance += abs(int(col1[i]) - int(col2[i]))
        similarity += int(col1[i]) * len([n for n in col2 if n == col1[i]])

    print(distance)
    print(similarity)

    
