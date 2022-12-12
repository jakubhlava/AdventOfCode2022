def draw_point(cycle, register, sprite):
    if (cycle-1) % 40 == 0:
        print()
    print(sprite[(cycle-register) % 40], end="")


with open("input.txt", "r") as f:
    commands = f.readlines()

interesting_cycles = [20, 60, 100, 140, 180, 220]
stored_values = {}
register = 1
cycle = 1
sprite = "###....................................."
print("Part 2:", end="")
for command in commands:
    argv = command.strip().split()
    draw_point(cycle, register, sprite)
    match argv[0]:
        case "addx":
            cycle += 2
            draw_point(cycle-1, register, sprite)
            if cycle-1 in interesting_cycles:
                stored_values[cycle-1] = register
            register += int(argv[1])
        case "noop":
            cycle += 1
    if cycle in interesting_cycles:
        stored_values[cycle] = register

print("\nPart 1:", sum([k*v for k, v in stored_values.items()]))
