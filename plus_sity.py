from collections import deque

# Чтение входных данных
n, m, d = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# Находим все клетки с 'X'
houses = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'X']

# Если нет жилых объектов, максимальный квадрат ограничен только размерами карты
if not houses:
    print(min(n, m))
    exit()

# Вычисляем минимальное манхэттенское расстояние до ближайшего 'X' для каждой клетки
dist = [[float('inf')] * m for _ in range(n)]
queue = deque(houses)
visited = set(houses)

for r, c in houses:
    dist[r][c] = 0

# BFS для вычисления расстояний
while queue:
    r, c = queue.popleft()
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
            dist[nr][nc] = dist[r][c] + 1
            visited.add((nr, nc))
            queue.append((nr, nc))

# Бинарный поиск по размеру квадрата
def can_place_square(k):
    # Проверяем все возможные позиции левого верхнего угла квадрата
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            # Находим минимальное расстояние до 'X' в квадрате k x k
            min_dist = float('inf')
            for r in range(i, i + k):
                for c in range(j, j + k):
                    min_dist = min(min_dist, dist[r][c])
                    if min_dist < d:  # Если нашли расстояние < d, квадрат не подходит
                        break
                if min_dist < d:
                    break
            if min_dist >= d:  # Если минимальное расстояние >= d, квадрат подходит
                return True
    return False

# Бинарный поиск для нахождения максимального k
left, right = 1, min(n, m)
result = 0
while left <= right:
    mid = (left + right) // 2
    if can_place_square(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)