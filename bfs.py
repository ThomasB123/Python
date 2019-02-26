
G = [[0,0,0,1,0,0,0,0],
    [1,0,0,0,1,0,1,1],
    [0,1,0,0,0,1,0,1],
    [1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0,0],
    [1,0,0,0,1,0,0,0],
    [0,1,0,0,1,0,0,0]]
s = 0

def BFS(G, s): # s is starting vertex
    # Colour code:
    # White - Undiscovered
    # Grey - Discovered but unprocessed (not fully explored)
    # Black - Has been processed (fully explored)
    colour = ['WHITE']*len(G)
    d = [1000]*len(G)
    π = [None]*len(G)
    colour[s] = 'GREY'
    d[s] = 0
    π[s] = None
    Q = []
    Q.append(s)
    Adj = []
    for x in G:
        Adj.append([])
    for x in range(len(G)):
        for y in range(len(G[x])):
            if G[x][y]:
                Adj[x].append(y)
    # Adj is the adjacency matrix
    print('Adj',Adj)
    while Q != []:
        u = Q.pop()
        for v in Adj[u]:
            if colour[v] == 'WHITE':
                colour[v] = 'GREY'
                d[v] = d[u] + 1
                π[v] = u
                Q.append(v)
        colour[u] = 'BLACK'
    print('colour',colour)
    print('d',d)
    print('π',π)

BFS(G,s)