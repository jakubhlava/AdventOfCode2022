with open("input.txt", "r") as f:
    rounds = [l.strip().split(" ") for l in f.readlines()]

pts = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
wins = {"A": "Y", "B": "Z", "C": "X"}
losses = {"A": "Z", "B": "X", "C": "Y"}

total_d1 = 0
total_d2 = 0
for r in rounds:
    total_d1 += pts[r[1]]
    if pts[r[0]] == pts[r[1]]:
        total_d1 += 3
    if wins[r[0]] == r[1]:
        total_d1 += 6
    match r[1]:
        case "X":
            total_d2 += pts[losses[r[0]]]
        case "Y":
            total_d2 += 3 + pts[r[0]]
        case "Z":
            total_d2 += 6 + pts[wins[r[0]]]

print("Part 1: ", total_d1)
print("Part 2: ", total_d2)
