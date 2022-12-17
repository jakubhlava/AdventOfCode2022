with open("input-sm.txt", "r") as f:
    valve_defs = f.read().splitlines()

valves = {}
ways = {}
for vd in valve_defs:
    name = vd[6:8]
    flow = int(vd.split(";")[0].split("=")[-1])
    next_ = vd.split(";")[1].strip().replace(",", "").split(" ")[4:]
    valves[name] = flow
    ways[name] = next_

current = "AA"
