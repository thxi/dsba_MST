import csv


def read_mat(mat):
    # reads the graph
    # and returns the list of edges
    edges = list()
    for (i, (_, row)) in enumerate(mat.iterrows()):
        for (j, vert) in enumerate(mat.columns[i+1:]):
            if (row[vert] == -1):
                continue
            edges.append((i, j + i + 1, row[vert]))
    return edges


def edges_to_csv(file_name, edges):
    with open('data/'+file_name+'.csv', 'w') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        w.writerow(['node1', 'node2', 'dist'])
        for i in range(len(edges)):
            w.writerow(edges[i])
