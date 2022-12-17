import sys
from itertools import cycle

import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize, linewidth=30)
class FallingShape:

    def __init__(self, chamber, chambertop):
        self.chamber = chamber
        self.position = [3, chambertop + 4]

    def move(self, direction):
        valid = self.validate(direction)
        if not valid:
            return False
        if direction == ">":
            self.position[0] += 1
        elif direction == "<":
            self.position[0] -= 1
        else:
            self.position[1] -= 1
        return True

    def validate(self, direction):
        pass

    def lay_down(self):
        pass

class FlatLyingShape(FallingShape):

    def validate(self, direction):
        if direction == ">" and self.chamber[self.position[1], self.position[0]+4] == 1:
            return False
        if direction == "<" and self.chamber[self.position[1], self.position[0]-1] == 1:
            return False
        if direction == "V" and np.sum(self.chamber[self.position[1]-1, self.position[0]:self.position[0]+4]) > 0:
            return False
        return True

    def lay_down(self):
        self.chamber[self.position[1], self.position[0]:self.position[0]+4] = 1
        return self.chamber

class PlusShape(FallingShape):
    def validate(self, direction):
        if direction == ">" and (self.chamber[self.position[1], self.position[0]+2] == 1 or self.chamber[self.position[1]+1, self.position[0]+3] == 1 or self.chamber[self.position[1]+2, self.position[0]+2] == 1):
            return False
        if direction == "<" and (self.chamber[self.position[1], self.position[0]] == 1 or self.chamber[self.position[1]+1, self.position[0]-1] == 1 or self.chamber[self.position[1]+2, self.position[0]] == 1):
            return False
        if direction == "V" and sum([self.chamber[self.position[1], self.position[0]], self.chamber[self.position[1]-1, self.position[0]+1], self.chamber[self.position[1], self.position[0]+2]]) > 0:
            return False
        return True

    def lay_down(self):
        self.chamber[self.position[1], self.position[0]+1] = 1
        self.chamber[self.position[1]+1, self.position[0]:self.position[0]+3] = 1
        self.chamber[self.position[1]+2, self.position[0] + 1] = 1
        return self.chamber

class LShape(FallingShape):

    def validate(self, direction):
        if direction == ">" and 1 in self.chamber[self.position[1]:self.position[1]+3, self.position[0]+3]:
            return False
        if direction == "<" and (1 in self.chamber[self.position[1]+1:self.position[1]+3, self.position[0]+1] or self.chamber[self.position[1], self.position[0]-1] == 1):
            return False
        if direction == "V" and 1 in self.chamber[self.position[1]-1, self.position[0]:self.position[0]+3]:
            return False
        return True

    def lay_down(self):
        self.chamber[self.position[1], self.position[0]:self.position[0]+3] = 1
        self.chamber[self.position[1]:self.position[1]+3, self.position[0]+2] = 1
        return self.chamber

class IShape(FallingShape):

    def validate(self, direction):
        if direction == ">" and 1 in self.chamber[self.position[1]:self.position[1]+4, self.position[0]+1]:
            return False
        if direction == "<" and 1 in self.chamber[self.position[1]:self.position[1]+4, self.position[0]-1]:
            return False
        if direction == "V" and self.chamber[self.position[1]-1, self.position[0]] == 1:
            return False
        return True

    def lay_down(self):
        self.chamber[self.position[1]:self.position[1]+4, self.position[0]] = 1
        return self.chamber

class BlockShape(FallingShape):

    def validate(self, direction):
        if direction == ">" and np.sum(self.chamber[self.position[1]:self.position[1]+2, self.position[0]+2]) > 0:
            return False
        if direction == "<" and np.sum(self.chamber[self.position[1]:self.position[1]+2, self.position[0]-1]) > 0:
            return False
        if direction == "V" and np.sum(self.chamber[self.position[1]-1, self.position[0]:self.position[0]+2]) > 0:
            return False
        return True

    def lay_down(self):
        self.chamber[self.position[1]:self.position[1]+2, self.position[0]:self.position[0]+2] = 1
        return self.chamber

def get_chamber_top(chamber):
    indices = np.nonzero(chamber[1:, 1:8])
    if len(indices[0]) == 0:
        return 0
    return max(indices[0])+1

with open("input.txt", "r") as f:
    moves = f.read().strip()

chamber = np.zeros((100000, 9), dtype=np.int32)
chamber[0, :] = 1
chamber[:, 0] = 1
chamber[:, 8] = 1
chambertop = 0
dir_ = cycle(moves)
shapes = cycle([FlatLyingShape, PlusShape, LShape, IShape, BlockShape])
shapenum = 0
movenum = 0
oldmovenum = 0
lastcycletop = 0
lastcyclemove = 0
lastcycleshape = 0

for i in range(2022):
    shape = next(shapes)(chamber, get_chamber_top(chamber))
    shapenum = (shapenum + 1) % 5
    while True:
        shape.move(next(dir_))
        movenum = (movenum + 1) % len(moves)
        if not shape.move("V"):
            chamber = shape.lay_down()
            break
print("Part 1:", get_chamber_top(chamber))

chamber = np.zeros((100000, 9), dtype=np.int32)
chamber[0, :] = 1
chamber[:, 0] = 1
chamber[:, 8] = 1
chambertop = 0
dir_ = cycle(moves)
shapes = cycle([FlatLyingShape, PlusShape, LShape, IShape, BlockShape])
shapenum = 0
movenum = 0
oldmovenum = 0
lastcycletop = 0
lastcyclemove = 0
lastcycleshape = 0
difftop = 0
diffshape = 0
firstshape = 0
firsttop = 0
diff = 0

# not working for example
for i in range(6000):
    shape = next(shapes)(chamber, get_chamber_top(chamber))
    shapenum = (shapenum + 1) % 5
    while True:
        shape.move(next(dir_))
        movenum = (movenum + 1) % len(moves)
        if not shape.move("V"):
            chamber = shape.lay_down()
            break
    if movenum < oldmovenum:
        if firstshape == 0:
            firstshape = i
            firsttop = get_chamber_top(chamber)
        if lastcyclemove == movenum:
            difftop = get_chamber_top(chamber) - lastcycletop
            diffshape = i - lastcycleshape
        lastcycleshape = i
        lastcyclemove = movenum
        lastcycletop = get_chamber_top(chamber)

    if i == lastcycleshape + 1441:
        diff = get_chamber_top(chamber)-lastcycletop
        if difftop != 0 and diffshape != 0:
            break
    oldmovenum = movenum

print("Part 2:", ((1000000000000 - firstshape)//diffshape)*difftop + firsttop + diff)

