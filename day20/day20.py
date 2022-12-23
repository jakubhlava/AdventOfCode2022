with open("input.txt", "r") as f:
    orig_nums = list(map(int, f.read().splitlines()))

def mix(numbers, default_state):
    for number in default_state:
        position = numbers.index(number)
        newpos = position + number[1]
        newpos %= (len(numbers) - 1)
        numbers.pop(position)
        numbers.insert(newpos, number)
    return numbers

p1_nums = [(i, num) for i, num in enumerate(orig_nums)]
p1_default = [(i, num) for i, num in enumerate(orig_nums)]
p2_nums = [(i, num*811589153) for i, num in p1_nums]
p2_default = [(i, num*811589153) for i, num in p1_nums]

numbers = mix(p1_nums, p1_default)
zero = numbers.index([n for n in p1_default if n[1] == 0][0])
print("Part 1:", numbers[(1000+zero)%len(numbers)][1]+numbers[(2000+zero)%len(numbers)][1]+numbers[(3000+zero)%len(numbers)][1])

for _ in range(10):
    p2_nums = mix(p2_nums, p2_default)
p2_zero = p2_nums.index([n for n in p2_default if n[1] == 0][0])
print("Part 2:", p2_nums[(1000+p2_zero)%len(p2_nums)][1]+p2_nums[(2000+p2_zero)%len(p2_nums)][1]+p2_nums[(3000+p2_zero)%len(p2_nums)][1])