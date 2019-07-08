import pandas as pd
import sys
import folium
from folium.plugins import MarkerCluster


def make_map(edges, coord, file_name, postfix, markers=False):
    m = folium.Map(
        location=[61.254035, 73.396221],
        zoom_start=3,
        tiles='CartoDB positron'
    )

    used = dict()
    for (_, edge) in edges.iterrows():
        city1, city2 = edge['node1'], edge['node2']
        p1, p2 = coord[city1], coord[city2]
        folium.PolyLine([p1, p2]).add_to(m)
        if markers:
            if (city1 not in used):
                used[city1] = 0
                folium.Marker([p1[0], p1[1]], popup=city1,
                              icon=folium.Icon(icon='circle')).add_to(m)
            if (city2 not in used):
                used[city2] = 0
                folium.Marker([p2[0], p2[1]], popup=city2,
                              icon=folium.Icon(icon='circle')).add_to(m)

    if markers:
        file_name += '_markers'
    m.save('maps/'+file_name+postfix+'.html')


if __name__ == '__main__':
    algs = ['boruvka', 'prim', 'kruskal']
    file_base = 'data/mst_'
    postfix = 'v1'
    if (len(sys.argv) != 1):
        postfix = sys.argv[1]
    postfix = '_'+postfix

    cities = pd.read_csv('data/ru_lat_lng_clear.csv')

    coord = dict()
    for (_, city) in cities.iterrows():
        coord[city['name']] = (city['lat'], city['lng'])

    for alg in algs:

        file_name = file_base+alg+postfix
        print(file_name)
        edges = pd.read_csv(file_name+'.csv')

        make_map(edges, coord, alg+'_map', postfix)
        make_map(edges, coord, alg+'_map', postfix, True)
