import math

def main(n, m):
    a = m + n
    print(math.floor(math.sqrt(a)))

if __name__ == '__main__':

    n, m = map(int, input().split())
    main(n, m)
