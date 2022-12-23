import numpy as np
import re

with open("input-sm.txt", "r") as f:
    board_str, moves_str = f.read().split("\n\n")
    board_lns = [list(ln) for ln in board_str.splitlines()]
    board = np.zeros((len(board_lns), max([len(ln) for ln in board_lns])), dtype=np.int8)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            try:
                if board_lns[i][j] == ".":
                    board[(i, j)] = 1
                elif board_lns[i][j] == "#":
                    board[(i, j)] = 2
            except IndexError:
                pass
    match = re.findall(r"[0-9]+[LR]?", moves_str)
    moves = []
    for m in match:
        if m[-1] in ["L", "R"]:
            moves.append(int(m[:-1]))
            moves.append(m[-1])
        else:
            moves.append(int(m))


def wrap_around(pos, facing, board):
    match facing:
        case 0:
            return pos[0], np.argwhere(board[pos[0]])[0][0]
        case 1:
            return np.argwhere(board[:, pos[1]])[0][0], pos[1]
        case 2:
            return pos[0], np.argwhere(board[pos[0]])[-1][0]
        case 3:
            return np.argwhere(board[:, pos[1]])[-1][0], pos[1]


pos = (0, np.argwhere(board[0])[0][0])
facing = 0
print(board.shape)

for move in moves:
    if move == "L":
        facing = (facing - 1) % 4
    elif move == "R":
        facing = (facing + 1) % 4
    else:
        for i in range(move):
            match facing:
                case 0:
                    next_pos = (pos[0], pos[1] + 1)
                case 1:
                    next_pos = (pos[0] + 1, pos[1])
                case 2:
                    next_pos = (pos[0], pos[1] - 1)
                case _:
                    next_pos = (pos[0] - 1, pos[1])
            if next_pos[0] >= board.shape[0] or next_pos[1] >= board.shape[1] or next_pos[0] < 0 or next_pos[1] < 0 or \
                    board[next_pos] == 0:
                next_pos = wrap_around(pos, facing, board)
            if board[next_pos] in [0, 2]:
                next_pos = pos
            pos = next_pos

print("Part 1:", 1000*(pos[0]+1)+4*(pos[1]+1)+facing)
