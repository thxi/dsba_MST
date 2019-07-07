from math import inf


def find_smallest(keys, mst):
    m = inf
    mi = -1
    for i in range(len(keys)):
        if (i not in mst and keys[i] < m):
            m = keys[i]
            mi = i
    return mi


def prim(nodes, mat, cols):
    # nodes - the number of nodes in the graph
    # mat - adjacency matrix
    # cols - the list of the names of each node
    # example: nodes = 3, cols = ['A', 'B', 'C'] meaning that
    # node "0" is 'A'
    # node "1" is 'B'
    # node "2" is 'C'

    # list of parent vertices
    parent = list(range(nodes))
    # set of vertices included in mst
    mst = set()
    # keys of vertices
    keys = [inf for i in range(nodes)]
    # Picking a random vertex
    keys[0] = 0

    while len(mst) != nodes:
        u = find_smallest(keys, mst)
        mst.add(u)
        # print("Add {}".format(u))

        # updating keys
        for i in range(len(mat[u])):
            if (mat[u][i] > 0 and (i not in mst)
                    and keys[i] > mat[u][i]):
                keys[i] = mat[u][i]
                parent[i] = u

    # list of spanning tree edges
    s_edges = list()

    for i in range(1, nodes):
        s_edges.append((cols[i], cols[parent[i]], mat[i][parent[i]]))
        # print("{}-{} {}".format(cols[parent[i]], cols[i], mat[i][parent[i]]))

    return s_edges
