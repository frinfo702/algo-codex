# 文字列を毎回コピーするので遅い。
# 間に合わない
# 意外と文字列のコピーは時間がかかる。
# 長さLならO(L)
import sys

input = sys.stdin.readline

pc_num, query_num = map(int, input().split())
queries = [[""]] * (query_num + 1)
for idx in range(1, query_num + 1):
    queries[idx] = input().split()

server = ""
pcs = [""] * (pc_num + 1)

for q in queries[1:]:
    query_type = int(q[0])
    if query_type == 1:
        pc_idx = int(q[1])
        pcs[pc_idx] = server
    elif query_type == 2:
        pc_idx = int(q[1])
        target = q[2]
        pcs[pc_idx] += target
    elif query_type == 3:
        pc_idx = int(q[1])
        server = pcs[pc_idx]
print(server)
