import copy

with open("input.txt", "r") as f:
    inp = f.readlines()

splitter = inp.index("\n")
column_defs = inp[:splitter-1]
column_maxsize = max([len(col)//4 for col in column_defs])

columns = [[] for _ in range(column_maxsize)]
for line in reversed(column_defs):
    for i in range(column_maxsize):
        try:
            if line[i*4+1] != " ":
                columns[i].append(line[i*4+1])
        except IndexError:
            pass
columns2 = copy.deepcopy(columns)

commands = inp[splitter+1:]
for command in commands:
    parted = command.strip().split(" ")
    amount, src, dest = int(parted[1]), int(parted[3])-1, int(parted[5])-1
    for _ in range(amount):
        columns[dest].append(columns[src].pop())
    columns2[dest].extend(columns2[src][-amount:])
    columns2[src] = columns2[src][:-amount]

print(f"Part 1: {''.join([c[-1] for c in columns])}")
print(f"Part 2: {''.join([c[-1] for c in columns2])}")