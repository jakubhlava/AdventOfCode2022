with open("input.txt", "r") as f:
    pairs = f.read().split("\n\n")

IN_ORDER, OUT_OF_ORDER, DONT_KNOW = 0, 1, 2


def compare_lists(left, right):
    i = 0
    while i < len(right):
        try:
            if isinstance(left[i], int) and isinstance(right[i], int):
                if left[i] == right[i]:
                    i += 1
                else:
                    return IN_ORDER if left[i] < right[i] else OUT_OF_ORDER
            elif isinstance(left[i], list) and isinstance(right[i], list):
                result = compare_lists(left[i], right[i])
                if result == DONT_KNOW:
                    i += 1
                else:
                    return result
            else:  # mixed types
                if isinstance(left[i], int):
                    result = compare_lists([left[i]], right[i])
                    if result == DONT_KNOW:
                        i += 1
                    else:
                        return result
                else:
                    result = compare_lists(left[i], [right[i]])
                    if result == DONT_KNOW:
                        i += 1
                    else:
                        return result
        except IndexError:
            return IN_ORDER
    return DONT_KNOW if len(left) == len(right) else OUT_OF_ORDER  # right longer


inorder = 0
for i, pair in enumerate(pairs):
    left_str, right_str = pair.strip().split("\n")
    left, right = None, None
    exec(f"left = {left_str}")
    exec(f"right = {right_str}")
    if compare_lists(left, right) == 0:
        inorder += i + 1

print(f"Part 1: {inorder}")

with open("input.txt", "r") as f:
    packets_str = f.read().strip().replace("\n\n", "\n").splitlines()
    packets_str.extend(["[[2]]", "[[6]]"])

packets = []
for p in packets_str:
    exec(f"packets.append({p})")

for _ in range(len(packets)):
    for i in range(len(packets)-1):
        if compare_lists(packets[i], packets[i+1]) == OUT_OF_ORDER:
            packet = packets.pop(i+1)
            packets.insert(i, packet)

print(f"Part 2: {(packets.index([[2]])+1)*(packets.index([[6]])+1)}")