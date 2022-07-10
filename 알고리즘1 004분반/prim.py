# Prim's Algorithm in Python

INF = 9999999
# number of vertices in graph
N = 10
#creating graph by adjacency matrix method
G = [[0, 32, 0, 17, 0, 0, 0, 0, 0, 0],
     [32, 0, 0, 0, 45, 0, 0, 0, 0, 0],
     [0, 0, 0, 18, 0, 0, 5, 0, 0, 0],
     [17, 0, 18, 0, 10, 0, 0, 3, 0, 0],
     [0, 45, 0, 10, 0, 28, 0, 0, 25, 0],
     [0, 0, 0, 0, 28, 0, 0, 0, 0, 6],
     [0, 0, 5, 0, 0, 0, 0, 59, 0, 0],
     [0, 0, 0, 3, 0, 0, 59, 0, 4, 0],
     [0, 0, 0, 0, 25, 0, 0, 4, 0, 12],
     [0, 0, 0, 0, 0, 6, 0, 0, 12, 0]]

selected_node = [0]*N

no_edge = 0


selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print("v" + str(1+a) + "-" + "v"+ str(1+b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1