def is_neighbour(head_, tail_):
    return abs(head_[0] - tail_[0]) <= 1 and abs(head_[1] - tail_[1]) <= 1


def fix_tail(head_, tail_):
    if not is_neighbour(head_, tail_):
        if head_[0] == tail_[0] and head_[1] != tail_[1]:
            tail_[1] += int((head_[1] - tail_[1]) / 2)
        elif head_[1] == tail_[1] and head_[0] != tail_[0]:
            tail_[0] += int((head_[0] - tail_[0]) / 2)
        else:
            tail_[0] += int(round((head_[0] - tail_[0]) / abs(head_[0] - tail_[0])))
            tail_[1] += int(round((head_[1] - tail_[1]) / abs(head_[1] - tail_[1])))
    return head_, tail_


with open("input.txt", "r") as f:
    commands = f.readlines()

head = [0, 0]
tail = [0, 0]
p2_chain = [[0, 0] for _ in range(10)]
visited = {(0, 0)}
visited_p2 = {(0, 0)}
for c in commands:
    direction, amount = c.split(" ")
    for i in range(int(amount)):
        match direction:
            case "R":
                head[0] += 1
                p2_chain[0][0] += 1
            case "L":
                head[0] -= 1
                p2_chain[0][0] -= 1
            case "U":
                head[1] += 1
                p2_chain[0][1] += 1
            case "D":
                head[1] -= 1
                p2_chain[0][1] -= 1
        head, tail = fix_tail(head, tail)
        visited.add(tuple(tail))
        for i in range(1, 10):
            p2_chain[i-1], p2_chain[i] = fix_tail(p2_chain[i-1], p2_chain[i])
        visited_p2.add(tuple(p2_chain[-1]))

print("Part 1:", len(visited))
print("Part 2:", len(visited_p2))