import copy
def next_pos(pos, blocked):
    if (pos[0], pos[1]+1) not in blocked:
        return pos[0], pos[1] + 1
    elif (pos[0]-1, pos[1]+1) not in blocked:
        return pos[0] - 1, pos[1] + 1
    elif (pos[0]+1, pos[1]+1) not in blocked:
        return pos[0] + 1, pos[1] + 1
    else:
        return pos

with open("input.txt", "r") as f:
    paths = f.read().splitlines()

lines = []
for path in paths:
    coords = [tuple(map(int, c.split(","))) for c in path.strip().split(" -> ")]
    for i in range(len(coords)-1):
        lines.append((coords[i], coords[i+1]))

blocked = set()
for left, right in lines:
    if left[0] == right[0]:
        if left[1] < right[1]:
            blocked.update([(left[0], x) for x in range(left[1], right[1]+1)])
        else:
            blocked.update([(left[0], x) for x in range(right[1], left[1] + 1)])
    else:
        if left[0] < right[0]:
            blocked.update([(x, left[1]) for x in range(left[0], right[0]+1)])
        else:
            blocked.update([(x, left[1]) for x in range(right[0], left[0] + 1)])
floor = max([x[1] for x in blocked])
width = (min([x[0] for x in blocked]), max([x[0] for x in blocked]))
blocked_p2 = copy.deepcopy(blocked)
blocked_p2.update([(x, floor+2) for x in range(width[0]-floor, width[1]+floor)])

sand = 0
while True:
    pos = (500, 0)
    while True:
        nxt = next_pos(pos, blocked)
        if nxt == pos:
            blocked.add(pos)
            sand += 1
            break
        elif nxt[1] > floor:
            break
        else:
            pos = nxt
    if nxt[1] > floor:
        break

print("Part 1:", sand)

sand = 0
while True:
    pos = (500, 0)
    while True:
        nxt = next_pos(pos, blocked_p2)
        if nxt == pos:
            blocked_p2.add(pos)
            sand += 1
            break
        else:
            pos = nxt
    if nxt == (500, 0):
        break

print("Part 2:", sand)