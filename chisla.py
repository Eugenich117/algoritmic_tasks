
def main():
    a, b, c = map(int, input().split())
    if a < b < c:
        print(b)
    if b < a < c:
        print(a)
    elif a < c < b:
        print(c)

if __name__ == '__main__':
    main()