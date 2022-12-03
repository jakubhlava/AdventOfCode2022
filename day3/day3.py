def priority(item):
    prio = ord(item) + 1 - ord("A")
    if prio > 26:  # srovnání malých znaků do pořadí
        prio -= (ord("a") - ord("A"))
    else:  # prohození malých a velkých písmen
        prio += 26
    return prio


def find_common(first, second):
    return set(first).intersection(set(second))


with open("input.txt", "r") as f:
    rucksacks = [l.strip() for l in f.readlines()]

total_priority = sum(priority(find_common(r[:len(r) // 2], r[len(r) // 2:]).pop())
                     for r in rucksacks)
total_priority2 = sum(priority(find_common(rucksacks[i], find_common(rucksacks[i + 1], rucksacks[i + 2])).pop())
                      for i in range(0, len(rucksacks), 3))

print("Part 1:", total_priority)
print("Part 2:", total_priority2)
