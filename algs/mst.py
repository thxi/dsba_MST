import boruvka
import prim
import kruskal
import utils
import sys
import pandas as pd

if __name__ == '__main__':
    file_name = 'data/ru_dist_mat'
    postfix = 'v1'
    if (len(sys.argv) != 1):
        postfix = sys.argv[1]
    postfix = '_'+postfix
    print(file_name+postfix)

    mat = pd.read_csv(file_name+postfix+'.csv', index_col='name')

    nodes = len(mat.columns)
    edges = utils.read_mat(mat)
    cols = mat.columns

    boruvka_edges = boruvka.boruvka(nodes, edges, cols)
    kruskal_edges = kruskal.kruskal(nodes, edges, cols)
    prim_edges = prim.prim(nodes, mat.values, cols)

    utils.edges_to_csv('mst_boruvka'+postfix, boruvka_edges)
    utils.edges_to_csv('mst_kruskal'+postfix, kruskal_edges)
    utils.edges_to_csv('mst_prim'+postfix, prim_edges)
