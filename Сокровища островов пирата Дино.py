n, m = map(int, input().split())
values = list(map(int, input().split()))

# Матрица смежности
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = True
    graph[b][a] = True

# Динамика: dp[mask][last]
size = 1 << n
dp = [[-1] * n for _ in range(size)]

# Начальное состояние: посетили только остров 0 (остров 1 в 1-индексации)
start_mask = 1 << 0
dp[start_mask][0] = values[0]

answer = values[0]  # может просто остаться на старте

for mask in range(size):
    for last in range(n):
        if dp[mask][last] == -1:
            continue
        # Попробуем пойти в next
        for nxt in range(n):
            if (mask >> nxt) & 1:  # уже посещён
                continue
            if last != nxt and not graph[last][nxt]:  # нет ребра
                continue
            new_mask = mask | (1 << nxt)
            new_value = dp[mask][last] + values[nxt]
            if new_value > dp[new_mask][nxt]:
                dp[new_mask][nxt] = new_value
            if new_value > answer:
                answer = new_value

print(answer)