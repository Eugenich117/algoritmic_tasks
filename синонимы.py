
def main():
    n = int(input())
    word_list = []
    for i in range(n):
        a, b = input().split()
        word_list.append((a, b))
    word_find = input()
    for a, b in word_list:
        if word_find == a:
            print(b)
            break
        elif word_find == b:
            print(a)
            break


if __name__ == '__main__':
    main()

'''#засчитано
def main():
    n = int(input())
    word_dict = {}
    for _ in range(n):
        word_1, word_2 = input().split()
        word_dict[word_1] = word_2
    word_find = input()
    if word_find in word_dict:
        print(word_dict[word_find])
    else:
        for key, value in word_dict.items():
            if word_find == value:
                print(key)


if __name__ == '__main__':
    main()'''