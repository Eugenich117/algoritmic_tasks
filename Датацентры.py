from collections import defaultdict


def find_bridges(n, edges):
    """Находит мосты в графе с помощью DFS."""
    adj = defaultdict(list)
    for u, v in edges:3
        adj[u].append(v)
        adj[v].append(u)

    tin = [float('inf')] * (n + 1)
    low = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    time = [0]
    bridges = []

    def dfs(u):
        time[0] += 1
        tin[u] = low[u] = time[0]
        for v in adj[u]:
            if tin[v] == float('inf'):  # Не посещен
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.append((min(u, v), max(v, u)))  # Упорядочиваем ребра
            elif v != parent[u]:  # Обратное ребро
                low[u] = min(low[u], tin[v])

    for u in range(1, n + 1):
        if tin[u] == float('inf'):
            dfs(u)

    return bridges


def build_component_tree(n, edges, bridges):
    """Строит дерево компонент 2-связности."""
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    component = [-1] * (n + 1)
    comp_id = [0]

    def dfs_component(u, cid):
        component[u] = cid
        for v in adj[u]:
            if component[v] == -1 and (min(u, v), max(v, u)) not in bridges_set:
                dfs_component(v, cid)

    bridges_set = set((min(u, v), max(v, u)) for u, v in bridges)
    for u in range(1, n + 1):
        if component[u] == -1:
            comp_id[0] += 1
            dfs_component(u, comp_id[0])

    comp_adj = defaultdict(list)
    for u, v in bridges:
        cu, cv = component[u], component[v]
        comp_adj[cu].append(cv)
        comp_adj[cv].append(cu)

    comp_vertices = defaultdict(list)
    for u in range(1, n + 1):
        comp_vertices[component[u]].append(u)

    return comp_adj, comp_vertices, component


def find_new_edges(n, edges):
    """Находит минимальное количество новых ребер для 2-связности."""
    bridges = find_bridges(n, edges)
    if not bridges:
        return 0, []

    # Строим дерево компонент
    comp_adj, comp_vertices, component = build_component_tree(n, edges, bridges)

    # Находим листья
    leaves = []
    for c in comp_adj:
        if len(comp_adj[c]) == 1:
            leaves.append(c)

    # Минимальное количество новых ребер
    m = (len(leaves) + 1) // 2

    # Проверяем существующие ребра
    edges_set = set((min(u, v), max(v, u)) for u, v in edges)

    new_edges = []
    # Соединяем листья парами
    for i in range(0, len(leaves) - 1, 2):
        c1, c2 = leaves[i], leaves[i + 1]
        u, v = comp_vertices[c1][0], comp_vertices[c2][0]
        if (min(u, v), max(u, v)) not in edges_set:
            new_edges.append((u, v))
        else:
            # Если ребро уже существует, ищем другую вершину
            for u2 in comp_vertices[c1]:
                for v2 in comp_vertices[c2]:
                    if (min(u2, v2), max(u2, v2)) not in edges_set:
                        new_edges.append((u2, v2))
                        break
                else:
                    continue
                break

    # Для нечетного количества листьев
    if len(leaves) % 2 == 1:
        leaf = leaves[-1]
        for c in comp_adj:
            if c != leaf and leaf not in comp_adj[c]:
                u, v = comp_vertices[leaf][0], comp_vertices[c][0]
                if (min(u, v), max(u, v)) not in edges_set:
                    new_edges.append((u, v))
                    break
                else:
                    # Ищем другие вершины
                    for u2 in comp_vertices[leaf]:
                        for v2 in comp_vertices[c]:
                            if (min(u2, v2), max(u2, v2)) not in edges_set:
                                new_edges.append((u2, v2))
                                break
                        else:
                            continue
                        break

    return m, new_edges


def main():
    n, k = map(int, input().split())
    edges = []
    for _ in range(k):
        u, v = map(int, input().split())
        edges.append((u, v))

    m, new_edges = find_new_edges(n, edges)
    print(m)
    for u, v in new_edges:
        print(u, v)


if __name__ == "__main__":
    main()
