import operator

with open("input.txt", "r") as f:
    defs = f.read().splitlines()
operators = {"+": operator.add, "-": operator.sub, "/": operator.floordiv, "*": operator.mul}

def resolve_p1(monkeys):
    while not isinstance(monkeys["root"], int):
        for name, expr in monkeys.items():
            if not isinstance(expr, int):
                for i in [0, 2]:
                    try:
                        if isinstance(monkeys[expr[i]], int):
                            expr[i] = monkeys[expr[i]]
                    except KeyError:
                        pass
                if isinstance(expr[0], int) and isinstance(expr[2], int):
                    monkeys[name] = operators[expr[1]](expr[0], expr[2])
    return monkeys

monkeys = {}
for m in defs:
    name, expr = m.split(": ")
    try:
        monkeys[name] = int(expr)
    except ValueError:
        monkeys[name] = expr.split(" ")


print("Part 1:", resolve_p1(monkeys)["root"])
