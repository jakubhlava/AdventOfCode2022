def get_cube_neighbors(pos):
    return {(pos[0]+1, pos[1], pos[2]), (pos[0]-1, pos[1], pos[2]),
            (pos[0], pos[1]+1, pos[2]), (pos[0], pos[1]-1, pos[2]),
            (pos[0], pos[1], pos[2]+1), (pos[0], pos[1], pos[2]-1)}

with open("input.txt", "r") as f:
    cubes = {tuple(map(int, x)) for x in [ln.split(",") for ln in f.read().splitlines()]}

limit = (max([c[0] for c in cubes])+1, max([c[1] for c in cubes])+1, max(c[2] for c in cubes)+1)


def expand(pos):
    global limit
    visited = set()
    expandable = [pos]
    while len(expandable) > 0:
        ex = expandable.pop()
        visited.add(ex)
        neighbors = get_cube_neighbors(ex)
        for n in neighbors:
            if n[0] < 0 or n[0] > limit[0] or n[1] < 0 or n[1] > limit[1] or n[2] < 0 or n[2] > limit[2]:
                return True
            if n not in visited and n not in cubes:
                expandable.append(n)
    return False


free_sides = 0
for cube in cubes:
    free_sides += sum([1 for n in get_cube_neighbors(cube) if n not in cubes])

print("Part 1:", free_sides)

fs2 = 0
for cube in cubes:
    for n in get_cube_neighbors(cube):
        if n not in cubes and expand(n):
            fs2 += 1

print("Part 2:", fs2)
