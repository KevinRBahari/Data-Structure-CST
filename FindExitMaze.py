# Kevin Renaldi Bahari
# 陈凯文
# 202369990129

# python code

def reach(adj, x, y):
    visited = [0] * len(adj)
    return explore(adj, x, y, visited)

def explore(adj, x, y, visited):
    if x == y:
        return 1
    visited[x] = 1
    for neighbor in adj[x]:
        if visited[neighbor] == 0:
            if explore(adj, neighbor, y, visited):
                return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    x, y = map(int, input().split())
    print(reach(adj, x - 1, y - 1))
