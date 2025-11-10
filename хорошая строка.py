import sys


def main():
    letters = []
    n = int(input())
    for i in range(n):
        letters.append(int(input()))
    result = 0
    for i in range(n - 1):
        current = min(letters[i], letters[i + 1])
        result += current
    print(result)

if __name__ == '__main__':
    main()
