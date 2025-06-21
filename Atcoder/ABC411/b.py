station_num = int(input())
distances = input().split()

for i in range(0, station_num - 1):
    result = []
    result.append(int(distances[i]))
    for j in range(i + 1, station_num - 1):
        result.append(int(distances[j]) + result[-1])
    print(" ".join(str(x) for x in result))
