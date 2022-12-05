with open("input.txt", "r") as f:
    assignments = [[[int(x) for x in r.split("-")] for r in l.strip().split(",")] for l in f.readlines()]

contains = 0
overlaps = 0
for f, s in assignments:
    first = set(range(f[0], f[1]+1))
    second = set(range(s[0], s[1]+1))
    if first <= second or second <= first:
        contains += 1
    if first & second:
        overlaps += 1

print("Part 1:", contains)
print("Part 2:", overlaps)