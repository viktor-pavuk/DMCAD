def bfs(s,t,parent):
    global n,matrix
    vis =[False for i in range(n)] 
    q = list() 
    q.insert(0,s)
    vis[s]=True
    parent[s]=-1
    while len(q)!=0:
        u = q.pop()
        for i in range(n):
            if not vis[i] and matrix[u][i]>0:
                q.insert(0,i)
                parent[i]=u
                vis[i]=True
    return vis[t] 


def fordFulkerson(graph,s,t):
    global matrix,n,int_max
    matrix = graph
    int_max = float('inf')
    n = len(matrix)
    parent, max_flow = [0 for i in range(n)], 0
    while bfs(s,t,parent):
        path_flow = int_max
        v = t
        while v!=s:
            u = parent[v]
            path_flow = min(path_flow, matrix[u][v])
            v = parent[v] 
        v = t
        while v!=s: 
            u = parent[v]
            matrix[u][v]-= path_flow 
            matrix[v][u]+= path_flow 
            v = parent[v]
        max_flow += path_flow
    print(f"Максимальний потік з вершини {s} в {t}: {max_flow}")
    return max_flow