import numpy as np

with open("input.txt", "r") as f:
    trees = np.matrix([list(l.strip()) for l in f.readlines()])

visible = 0
scenics = []
for y in range(trees.shape[0]):
    for x in range(trees.shape[1]):
        if y == 0 or x == 0 or y == trees.shape[0]-1 or x == trees.shape[1]-1:
            visible += 1
        else:
            hiders = trees >= trees[y, x]
            left, right, up, down = hiders[y+1:, x], np.flip(hiders[:y, x]), hiders[y, x+1:], np.flip(hiders[y, :x])
            if 0 in [np.sum(left), np.sum(right), np.sum(up), np.sum(down)]:
                visible += 1
            scenic = 1
            for path in [left, right, up, down]:
                tree_count = 0
                for elem in path:
                    tree_count += 1
                    if elem:
                        break
                scenic *= tree_count
            scenics.append(scenic)

print("Part 1:", visible)
print("Part 2:", max(scenics))
