# Kevin Renaldi Bahari
# 陈凯文
# 202369990129

# python code


import sys

def dfs(adj, used, order, x):
    used[x] = 1
    for i in range(len(adj[x])):
        if not used[adj[x][i]]:
            dfs(adj, used, order, adj[x][i])
    order.append(x)

def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if not used[i]:
            dfs(adj, used, order, i)
    order.reverse()
    return order

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1)
