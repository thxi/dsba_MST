def find_root(root, i):
    # find returns the root of a tree with the element i
    if root[i] == i:
        return i
    return find_root(root, root[i])


def merge_trees(root, rank, x, y):
    # union unite the two sets based on their rank
    xroot = find_root(root, x)
    yroot = find_root(root, y)
    if rank[xroot] < rank[yroot]:
        root[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        root[yroot] = xroot
    else:
        root[yroot] = xroot
        rank[xroot] += 1


def boruvka(nodes, edges, cols):
    # nodes - the number of nodes in the graph
    # edges - the list of edges in the graph
    # each edge is a tuple(or a list) in the following format:
    # (node1(int), node2(int), distance(float))
    # cols - the list of the names of each node
    # example: nodes = 3, cols = ['A', 'B', 'C'] meaning that
    # node "0" is 'A'
    # node "1" is 'B'
    # node "2" is 'C'

    # returns the tree weight and
    # the edges in the minimum spanning tree

    # list of spanning tree edges
    s_edges = list()
    # list of roots of nodes
    root = list(range(nodes))
    # list of ranks of nodes
    rank = [0] * nodes

    # initializing each node as its own component
    components = nodes

    while components > 1:
        # stores cheapest edge for each component
        cheapest = [-1.0] * nodes
        # finding the cheapest edge for every component
        for i in range(len(edges)):
            u, v, w = edges[i]
            root_u = find_root(root, u)
            root_v = find_root(root, v)

            if root_u != root_v:
                if cheapest[root_u] == -1 or cheapest[root_u][2] > w:
                    cheapest[root_u] = (u, v, w)

                if cheapest[root_v] == -1 or cheapest[root_v][2] > w:
                    cheapest[root_v] = (u, v, w)

        # Consider the above picked cheapest edges and add them
        # to MST
        for node in range(nodes):

            # Check if cheapest for current set exists
            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                root_u = find_root(root, u)
                root_v = find_root(root, v)

                if root_u != root_v:
                    s_edges.append((cols[u], cols[v], w))
                    merge_trees(root, rank, root_u, root_v)
                    # print("% s-%s % f" %
                    #       (cols[u], cols[v], w))
                    components = components - 1

        cheapest = [-1.0] * nodes

    return s_edges
