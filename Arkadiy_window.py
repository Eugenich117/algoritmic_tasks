import time
import tracemalloc
import os

def measure_performance():
    # Тестируемый код
    # Считываем входные данные
    n, m, x, y = map(int, input().split())
    windows = [input().strip() for _ in range(n * x)]
    tracemalloc.start()  # Начинаем отслеживать аллокации памяти
    start_time = time.perf_counter()  # Замер времени начала
    # Порог для "бодрствующей" квартиры
    threshold = (x * y + 1) // 2

    # Счётчик бодрствующих квартир
    awake = 0

    # Преобразуем строки в списки для более быстрого доступа
    windows = [list(row) for row in windows]

    # Проходим по всем квартирам
    for i in range(0, n * x, x):  # этажи с шагом x
        for j in range(0, m * y, y):  # квартиры с шагом y
            # Подсчитываем горящие окна
            count = sum(windows[r][c] == 'X'
                        for r in range(i, i + x)
                        for c in range(j, j + y))
            if count >= threshold:
                awake += 1

    # Выводим результат
    print(awake)

    # Замер времени и памяти
    end_time = time.perf_counter()
    snapshot = tracemalloc.take_snapshot()  # Фиксируем текущие аллокации
    tracemalloc.stop()

    # Суммарное выделение памяти (включая освобожденные блоки)
    total_allocated = sum(stat.size for stat in snapshot.statistics("lineno"))

    print(f"Время выполнения: {end_time - start_time:.4f} сек")
    print(f"Пиковое использование памяти: {tracemalloc.get_traced_memory()[1] / 1024 / 1024:.4f} МБ")
    print(f"Суммарное выделение памяти: {total_allocated / 1024 / 1024:.4f} МБ")

measure_performance()