# https://www.acmicpc.net/problem/1063

import sys

input = sys.stdin.readline

MAX = 8
MOVE_DICT = {
    "R": [1, 0],
    "L": [-1, 0],
    "B": [0, -1],
    "T": [0, 1],
    "RT": [1, 1],
    "LT": [-1, 1],
    "RB": [1, -1],
    "LB": [-1, -1],
}


def check_out_board(x, y):
    if (x >= 0 and x < MAX) and y > 0 and y <= MAX:
        return True
    return False


king, stone, N = map(str, input().split())

king_idxs = [ord(king[0]) - ord("A"), int(king[1])]
stone_idxs = [ord(stone[0]) - ord("A"), int(stone[1])]


for _ in range(int(N)):
    move = input().strip()
    if (
        king_idxs[0] + MOVE_DICT[move][0] == stone_idxs[0]
        and king_idxs[1] + MOVE_DICT[move][1] == stone_idxs[1]
    ):
        if check_out_board(stone_idxs[0] + MOVE_DICT[move][0], stone_idxs[1] + MOVE_DICT[move][1]):
            stone_idxs[0] = stone_idxs[0] + MOVE_DICT[move][0]
            stone_idxs[1] = stone_idxs[1] + MOVE_DICT[move][1]
            king_idxs[0] = king_idxs[0] + MOVE_DICT[move][0]
            king_idxs[1] = king_idxs[1] + MOVE_DICT[move][1]
    elif check_out_board(king_idxs[0] + MOVE_DICT[move][0], king_idxs[1] + MOVE_DICT[move][1]):
        king_idxs[0] = king_idxs[0] + MOVE_DICT[move][0]
        king_idxs[1] = king_idxs[1] + MOVE_DICT[move][1]

print(f"{chr(ord('A') + king_idxs[0])}{king_idxs[1]}")
print(f"{chr(ord('A') + stone_idxs[0])}{stone_idxs[1]}")
