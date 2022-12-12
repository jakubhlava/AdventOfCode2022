import operator
import math


class Monkey:

    def __init__(self, p2=False, *input_lines):
        self.id = int(input_lines[0][:-1].split(" ")[1])
        self.items = [int(x) for x in input_lines[1].split(": ")[1].split(", ")]
        self.operation = input_lines[2].split(": ")[1][6:]
        self.divisible = int(input_lines[3].split(" ")[-1])
        self.true_dest = int(input_lines[4].split(" ")[-1])
        self.false_dest = int(input_lines[5].split(" ")[-1])
        self.p2 = p2
        self.inspections = 0

    def throw_away(self, contacts):
        while len(self.items) > 0:
            worry_level = self.items.pop(0)
            expr = self.operation.split(" ")
            ops = {"+": operator.add, "*": operator.mul}
            expr[0] = worry_level if expr[0] == "old" else int(expr[0])
            expr[2] = worry_level if expr[2] == "old" else int(expr[2])
            worry_level = ops[expr[1]](expr[0], expr[2])
            self.inspections += 1
            if not self.p2:
                worry_level //= 3
            destination = self.true_dest if worry_level % self.divisible == 0 else self.false_dest
            if self.p2:
                # optimalized by modular arithmethic over product of "divisible by" primes from input
                worry_level = worry_level % math.prod([m.divisible for m in contacts.values()])
            contacts[destination].items.append(worry_level)


def do_monkey_business(part):
    monkeys = {}
    for m in monkey_strs:
        monkey = Monkey(part == 2, *[x.strip() for x in m.split("\n")])
        monkeys[monkey.id] = monkey

    for i in range(20 if part == 1 else 10000):
        for monkey in monkeys.values():
            monkey.throw_away(monkeys)

    max_inspects = sorted([m.inspections for m in monkeys.values()], reverse=True)
    print(f"Part {part}:", max_inspects[0] * max_inspects[1])


with open("input.txt", "r") as f:
    monkey_strs = f.read().split("\n\n")

do_monkey_business(1)
do_monkey_business(2)
