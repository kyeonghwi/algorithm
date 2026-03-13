def find_parents(tree, node):
    parents = []
    current = node
    while True:
        found = False
        for parent, children in enumerate(tree):
            if current in children:
                parents.append(parent)
                current = parent
                found = True
                break
        if not found:
            break
    return parents


def find_lca(n1, n2, tree):
    ancestors = set()
    current = n1
    while True:
        ancestors.add(current)
        found = False
        for parent, children in enumerate(tree):
            if current in children:
                current = parent
                found = True
                break
        if not found:
            break

    current = n2
    while True:
        if current in ancestors:
            return current
        found = False
        for parent, children in enumerate(tree):
            if current in children:
                current = parent
                found = True
                break
        if not found:
            return -1

T = int(input())
for tc in range(1, T + 1):
    v, e, n1, n2 = map(int,input().split())
    arr = list(map(int,input().split()))

    nodes= [[] for _ in range(v+1)]
    for i in range(0,2 * e,2):
        parent = arr[i]
        child = arr[i + 1]
        nodes[parent].append(child)
    parents_n1 = find_parents(nodes, n1)
    parents_n2 = find_parents(nodes, n2)

    lca = find_lca(n1, n2, nodes)

    def dfs(idx):
        cnt = 1
        for child in nodes[idx]:
            cnt += dfs(child)
        return cnt
    sub = dfs(lca)
    print(f"#{tc} {lca} {sub}")