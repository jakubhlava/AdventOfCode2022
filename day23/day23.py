with open("input.txt", "r") as f:
    initial = f.read().splitlines()

def get_neighbors(pos):
    n = []
    for i in range(pos[0]-1, pos[0]+2):
        for j in range(pos[1]-1, pos[1]+2):
            if (i, j) != pos:
                n.append((i, j))
    return set(n)

def get_directional_neighbors(pos, direction):
    match direction:
        case 0:
            return {(pos[0] - 1, pos[1]), (pos[0] - 1, pos[1] + 1), (pos[0] - 1, pos[1] - 1)}
        case 1:
            return {(pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1] + 1)}
        case 2:
            return {(pos[0], pos[1] - 1), (pos[0] - 1, pos[1] - 1), (pos[0] + 1, pos[1] - 1)}
        case 3:
            return {(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)}

elves = {}
for i, ln in enumerate(initial):
    for j, char in enumerate(ln):
        if char == "#":
            elves[len(elves.keys())] = (i+1, j+1)

counter = 0
oldproposed = {}
while True:
    proposed = {}
    full = {e for e in elves.values()}
    for num, pos in elves.items():
        neighbors = get_neighbors(pos)
        if not neighbors.intersection(full):
            continue
        newpos = None
        for i in range(4):
           # print(num, pos, get_directional_neighbors(pos, (direction_ptr + i) % 4), (direction_ptr + i) % 4)
            neighbors = get_directional_neighbors(pos, (counter + i) % 4)
            if not neighbors.intersection(full):
                match (counter + i) % 4:
                    case 0:
                        newpos = (pos[0] - 1, pos[1])
                    case 1:
                        newpos = (pos[0] + 1, pos[1])
                    case 2:
                        newpos = (pos[0], pos[1] - 1)
                    case 3:
                        newpos = (pos[0], pos[1] + 1)
                break
        if newpos:
            if newpos in proposed.keys():
                proposed[newpos].append(num)
            else:
                proposed[newpos] = [num]

    for pos, elf_ids in proposed.items():
        if len(elf_ids) > 1:
            continue
        else:
            elves[elf_ids[0]] = pos

    counter += 1
    if counter == 10:
        miny = min([e[0] for e in elves.values()])
        minx = min([e[1] for e in elves.values()])
        maxy = max([e[0] for e in elves.values()])
        maxx = max([e[1] for e in elves.values()])

        print("Part 1:", (abs(maxy - miny) + 1) * (abs(maxx - minx) + 1) - len(elves.keys()))
    if proposed == oldproposed:
        print("Part 2:", counter-1)
        break
    else:
        oldproposed = proposed




