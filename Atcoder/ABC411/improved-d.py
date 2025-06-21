import sys

# 再帰の深さ上限を増やす（最後の文字列構築で必要になる場合がある）
sys.setrecursionlimit(2 * 10**6)
input = sys.stdin.readline

N, Q = map(int, input().split())

# 各ノードを(文字列の断片, 前のノードのインデックス)として格納
# node 0 は根となる空のノード
string_nodes = [("", -1)]

# サーバーとPCがstring_nodesのどのインデックスを指しているか
pointers = [0] * (N + 1)

for _ in range(Q):
    query = input().split()
    query_type = int(query[0])

    if query_type == 1:
        p = int(query[1])
        pointers[p] = pointers[0]
    elif query_type == 2:
        p = int(query[1])
        s = query[2]

        prev_node_idx = pointers[p]
        string_nodes.append((s, prev_node_idx))
        pointers[p] = len(string_nodes) - 1

    elif query_type == 3:
        p = int(query[1])
        pointers[0] = pointers[p]

# サーバーが指す最後のノードから遡って断片を集める
final_pieces = []
current_node_idx = pointers[0]

while current_node_idx != -1:
    piece, prev_idx = string_nodes[current_node_idx]
    final_pieces.append(piece)
    current_node_idx = prev_idx

final_string = "".join(reversed(final_pieces))
print(final_string)
