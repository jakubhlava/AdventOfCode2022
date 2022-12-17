with open("input-sm.txt", "r") as f:
    defs = f.read().splitlines()

def inradius(point1, point2, radius):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1]) <= radius

sensors = []
beacons = set()
for d in defs:
    sensor, beacon = [tuple(map(int, x.split(", "))) for x in d.replace("Sensor at ", "").replace(" closest beacon is at ", "").replace("x=", "").replace("y=", "").split(":")]
    sensors.append({"center": sensor, "radius": abs(sensor[0]-beacon[0])+abs(sensor[1]-beacon[1])})
    beacons.add(beacon)

minx, miny = min([sensor["center"][0] - sensor["radius"] for sensor in sensors]), min([sensor["center"][1] - sensor["radius"] for sensor in sensors])
maxx, maxy = max([sensor["center"][0] + sensor["radius"] for sensor in sensors]), max([sensor["center"][1] + sensor["radius"] for sensor in sensors])
#row_to_check = 2000000
row_to_check = 10

nobeacon = 0
print(sensors)
print(minx, maxx)

for i in range(minx, maxx+1):
    if (i, row_to_check) not in beacons:
        for sensor in sensors:
            if inradius((i, row_to_check), sensor["center"], sensor["radius"]):
                nobeacon += 1
                break
print("Part 1:", nobeacon)


limit = 20
borders = {i: list() for i in range(limit+1)}
for sensor in sensors:
    for i in range(-sensor["radius"], sensor["radius"]+1):
        xbegin = sensor["center"][0]-abs(i)
        xend = sensor["center"][0]+abs(i)
        ylevel = i+sensor["center"][1]
        if 0 <= ylevel <= limit:
            new = [xbegin if xbegin >= 0 else 0, xend if xend <= limit else limit]
            modified = False
            for b in borders[ylevel]:
                if b[0] <= new[0] and new[1] <= b[1]:
                    continue
                elif new[0] <= b[0] and b[1] <= new[1]:
                    b[0] = new[0]
                    b[1] = new[1]
                    modified = True
                elif new[0] <= b[0] <= new[1]+1:
                    b[0] = new[0]
                    modified = True
                elif new[0]-1 <= b[1] <= new[1]:
                    b[1] = new[1]
                    modified = True
            if not modified:
                print(borders[ylevel], new)
                borders[ylevel].append(new)
        else:
            continue

print(borders)