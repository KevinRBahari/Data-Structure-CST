# Kevin Renaldi Bahari
# 陈凯文
# 202369990129

# python code


def acyclic(adj):
    visited = [0 for _ in range(len(adj))]
    rec_stack = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        if not visited[i]:
            if dfs(adj, i, visited, rec_stack):
                return 1
    return 0

def dfs(adj, x, visited, rec_stack):
    visited[x] = 1
    rec_stack[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]] and dfs(adj, adj[x][i], visited, rec_stack):
            return 1
        elif rec_stack[adj[x][i]]:
            return 1
    rec_stack[x] = 0
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
