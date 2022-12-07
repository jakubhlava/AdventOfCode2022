class FileObject:

    def __init__(self, name: str, type: str, parent=None, size: int=None):
        self.name = name
        self.type = type
        self.parent = parent
        self.size = size
        self.children = []

    def get_size(self):
        if self.type == "file":
            return self.size
        else:
            return sum([c.get_size() for c in self.children])


with open("input.txt", "r") as f:
    commands = [l.strip() for l in f.readlines()]

dir_refs = []
root = FileObject("/", "dir")
current_dir = root
index = 0
while index < len(commands):
    cmd = commands[index].split(" ")
    if cmd[0] == "$":
        match cmd[1]:
            case "cd":
                match cmd[2]:
                    case "/":
                        pass
                    case "..":
                        if current_dir.name != "/":
                            current_dir = current_dir.parent
                    case _:
                        current_dir = [d for d in current_dir.children if d.name == cmd[2]][0]
            case "ls":
                try:
                    next_cmd = [c[0] for c in commands[index+1:]].index("$")
                except ValueError:
                    next_cmd = len(commands)
                output = commands[index+1:index+next_cmd+1]
                for o in output:
                    info = o.split(" ")
                    if info[0] == "dir":
                        new = FileObject(info[1], "dir", current_dir)
                        current_dir.children.append(new)
                        dir_refs.append(new)
                    else:
                        current_dir.children.append(FileObject(info[1], "file", current_dir, int(info[0])))
                index += next_cmd
        index += 1

sizes = [d.get_size() for d in dir_refs]
print("Part 1:", sum([s for s in sizes if s < 100000]))

to_free = 30000000 - (70000000 - root.get_size())
print("Part 2:", min([s for s in sizes if s >= to_free]))
