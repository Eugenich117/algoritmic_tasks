def main():
    n, m = map(int, input().split())

    # Читаем n строк матрицы
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Выводим матрицу в том же формате
    for i in range(n):
        # Преобразуем числа в строки и объединяем через пробел
        print(' '.join(map(str, matrix[i])))


if __name__ == "__main__":
    main()