import os
import sys

import numpy as np
np.set_printoptions(threshold=sys.maxsize, linewidth=99999999)
def neighbors(x, y, matrix):
    """Čtyřokolí daného bodu v matici"""
    n = []
    if x > 0:
        n.append((x-1, y))
    if x < matrix.shape[0]-1:
        n.append((x+1, y))
    if y > 0:
        n.append((x, y-1))
    if y < matrix.shape[1]-1:
        n.append((x, y+1))
    return n

def linear(point, matrix):
    """Linearizuje tuple s bodem v matici kvůli použití v hashovaných typech set adict"""
    return point[0] * matrix.shape[1] + point[1]

def pt(linear, matrix):
    """Reverzní funkce k linear"""
    return (linear // matrix.shape[1], linear % matrix.shape[1])

def extract_min(unvisited, dijkstra):
    """Najde nejlepší (s nejmenší cenou přechodu od známých) vrchol pro pokračování hledání cesty"""
    min = np.iinfo(np.int32).max
    mp = None
    for u in unvisited:
        point = pt(u, dijkstra)
        if dijkstra[point] < min:
            min = dijkstra[point]
            mp = point
    return mp

def compute_dijkstra(begin, matrix, target):
    """Modifikovaná implementace dijkstrova algoritmu s vyřazením netknutých bodů z hledání nejlepšího vrcholu extract_min"""
    dijkstra = np.ndarray(matrix.shape, dtype=np.int32)
    dijkstra[:] = np.iinfo(np.int32).max    # místo nekonečna maximánlí hodnota int32

    unvis_touched = {linear(begin, matrix)}  # nenavštívené modifikované
    previous = {}        # slovník s předky jednotlivých bodů
    dijkstra[begin] = 0  # první pole má nulovou cenu přechodu - začínáme zde
    while unvis_touched:
        best = extract_min(unvis_touched, dijkstra)     # hledání nejlepšího vrcholu
        unvis_touched.remove(linear(best, matrix))      # odstranění z množiny nenavštívených
        for n in neighbors(*best, matrix):              # přehodnocení sousedů
            if dijkstra[best] + 1 < dijkstra[n] and (matrix[n] <= matrix[best]+1):
                dijkstra[n] = dijkstra[best] + 1
                previous[linear(n, matrix)] = best
                unvis_touched.add(linear(n, matrix))
        if best[0] == target[0] and best[1] == target[1]:
            break
    return dijkstra

with open("input.txt", "r") as f:
    heightmap = np.array([list(map(lambda x: ord(x) - ord("a") + 1, list(ln))) for ln in f.read().replace("S", "`").split("\n") if ln != ""])


begin = tuple(np.argwhere(heightmap == 0)[0])
finish = tuple(np.argwhere(heightmap == ord("E") - ord("a") + 1)[0])
heightmap[finish] = ord("z") - ord("a") + 1
print("Part 1:", compute_dijkstra(begin, heightmap, finish)[finish])

possible_starts = list(map(tuple, np.argwhere(heightmap == 1)))
print("Part 2:", min(compute_dijkstra(begin, heightmap, finish)[finish] for begin in possible_starts))
