def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(nodes, edges, cols):

    result = []  # This will store the resultant MST
    i = 0  # An index variable, used for sorted edges
    e = 0  # An index variable, used for result[]

    # Sorting if all edges
    edges = sorted(edges, key=lambda x: x[2])

    parent = list(range(nodes))
    rank = [0] * nodes

    # Number of edges to be taken is equal to V-1
    while e < nodes - 1:

        # Construction of STree
        u, v, w = edges[i]
        i = i + 1

        if (w == -1):
            continue

        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does't cause cycle,
        # include it in result and increment the index
        # of result for next edge
        if x != y:
            e = e + 1
            result.append([cols[u], cols[v], w])
            # print("{} -- {} == {}".format(cols[u], cols[v], w))
            union(parent, rank, x, y)

    return result
