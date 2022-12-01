with open("input.txt", "r") as f:
    input_vals = f.readlines()

elves = [0]
for val in input_vals:
    if val == "\n":
        elves.append(0)
    else:
        elves[-1] += int(val)

print(f"Part 1: {max(elves)}")
print(f"Part 2: {sum(sorted(elves, reverse=True)[:3])}")
