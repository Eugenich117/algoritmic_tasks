from collections import deque
import sys


def main():
    input = sys.stdin.read
    data = input().split()

    n, k = int(data[0]), int(data[1])
    arr = list(map(int, data[2:2 + n]))

    dq = deque()
    result = []

    for i in range(n):
        # Убираем элементы, выходящие за левую границу окна
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Убираем с конца элементы, которые больше или равны текущему
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()

        dq.append(i)

        # Начиная с (k-1)-го элемента можно выводить минимум
        if i >= k - 1:
            result.append(str(arr[dq[0]]))

    sys.stdout.write("\n".join(result))


if __name__ == '__main__':
    main()