with open("input.txt", "r") as f:
    buffer = f.read().strip()

p1solved = False
for i in range(len(buffer)-14):
    if len(set(buffer[i:i+4])) == 4 and not p1solved:
        print("Part 1:", i+4)
        p1solved = True
    if len(set(buffer[i:i+14])) == 14:
        print("Part 2:", i+14)
        break