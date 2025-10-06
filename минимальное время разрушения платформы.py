def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    h = list(map(int, data[1:1 + N]))

    ans = [-1] * N

    # Обработка чётных индексов
    stack = []
    for i in range(N - 1, -1, -1):
        if i % 2 == 0:
            while stack and stack[-1][0] <= h[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1][1] - i
            stack.append((h[i], i))

    # Обработка нечётных индексов
    stack = []
    for i in range(N - 1, -1, -1):
        if i % 2 == 1:
            while stack and stack[-1][0] <= h[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1][1] - i
            stack.append((h[i], i))

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    solve()