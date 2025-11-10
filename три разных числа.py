def main():
    n = int(input())
    if n == 0:
        print(1)
        return
    elif n == 1:
        print(2)
        return

    a0, a1, a2 = 1, 1, 0
    for i in range(2, n + 1):
        new_a0 = a0 + a1 + a2
        new_a1 = a0
        new_a2 = a1
        a0, a1, a2 = new_a0, new_a1, new_a2

    total = a0 + a1 + a2
    print(total)


if __name__ == '__main__':
    main()