import sys


def solve():
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    idx = 1
    queries = []

    # Читаем запросы
    for _ in range(N):
        M_i = int(data[idx]);
        idx += 1
        words = data[idx].split();
        idx += 1
        queries.append(set(words))

    # Словарь: слово -> список индексов запросов, содержащих это слово
    word_to_queries = {}
    for i, words_set in enumerate(queries):
        for word in words_set:
            if word not in word_to_queries:
                word_to_queries[word] = []
            word_to_queries[word].append(i)

    # DSU для запросов
    parent = list(range(N))
    rank = [0] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1

    # Объединяем запросы, имеющие общие слова
    for indices in word_to_queries.values():
        if len(indices) > 1:
            first = indices[0]
            for j in range(1, len(indices)):
                union(first, indices[j])

    # Группируем запросы по компонентам
    components = {}
    for i in range(N):
        root = find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    # Для каждой компоненты объединяем слова
    max_size = 0
    for comp_indices in components.values():
        words_union = set()
        for q_idx in comp_indices:
            words_union |= queries[q_idx]  # объединение множеств
        max_size = max(max_size, len(words_union))

    num_contexts = len(components)
    print(num_contexts, max_size)


if __name__ == "__main__":
    solve()