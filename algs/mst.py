import boruvka
import prim
import kruskal
import utils
import sys
import pandas as pd

if __name__ == '__main__':
    algs = ['boruvka', 'prim', 'krurkal']
    file_name = 'data/ru_dist_mat_v1.csv'
    if (len(sys.argv) == 1):
        print(file_name)
    mat = pd.read_csv(file_name, index_col='name')

    nodes = len(mat.columns)
    edges = utils.read_mat(mat)
    cols = mat.columns

    boruvka_edges = boruvka.boruvka(nodes, edges, cols)
    kruskal_edges = kruskal.kruskal(nodes, edges, cols)
    prim_edges = prim.prim(nodes, mat.values, cols)

    utils.edges_to_csv('mst_boruvka', boruvka_edges)
    utils.edges_to_csv('mst_kruskal', kruskal_edges)
    utils.edges_to_csv('mst_prim', prim_edges)
