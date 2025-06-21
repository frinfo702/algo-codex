import sys

WHITE = 0
BLACK = 1

input = sys.stdin.readline

N, Q = map(int, input().split())
queries = list(map(int, input().split()))

oseros = [WHITE] * int(N + 2)  # sentinel

count = 0
for q_idx in queries:
    left_is_black = oseros[q_idx - 1] == BLACK
    right_is_black = oseros[q_idx + 1] == BLACK

    if oseros[q_idx] == WHITE:
        if left_is_black and right_is_black:
            count -= 1
        elif not left_is_black and not right_is_black:
            count += 1
    elif oseros[q_idx] == BLACK:
        if left_is_black and right_is_black:
            count += 1
        elif not left_is_black and not right_is_black:
            count -= 1
    oseros[q_idx] = 1 - oseros[q_idx]
    print(count)
