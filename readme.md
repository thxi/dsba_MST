Visualization
---
Data visualization can be found [HERE](https://dsba.herokuapp.com)
> WARNING: yandex map might take some time to load

The buttons and the tabs should be pretty self-explanatory

* boruvka/kruskal/prim - the tab showcasing the obtained mst (which is unique considering the circumstances) using the algorithm
* comparison - the tab which shows how the distances compare to existing ones. The lower the opacity of the road, the higher the difference in length between the existing road and the blue one; Lines are clickable
* Yandex map - the map which uses yandex js api to create the map inplace to show the real and 'imaginary' roads on one map

---

To run locally you need [docker](https://www.docker.com/)

Then:
```bash
make build-front
make run-front # runs on localhost:1337

make kill-front # to stop the container
```


Miscellaneous:
---
Obtained coordinates of cities can be found in [data/ru_lat_lng.csv](https://github.com/thxi/dsba/blob/master/data/ru_dist_mat.csv) or [jupyter/cities->edges.ipynb](https://github.com/thxi/dsba/blob/master/jupyter/cities-%3Eedges.ipynb)

That dataset contained some outliers which had to be deleted;

The corresponding jupyter notebook: [jupyter/city_outliers.ipynb](https://github.com/thxi/dsba/blob/master/jupyter/city_outliers.ipynb)

Clear dataset: [ru_lat_lng_clear.csv](https://github.com/thxi/dsba/blob/master/data/ru_lat_lng_clear.csv)

---

The distance between cities was calculated according to the Vincenty's formulae (see [great circle distance](https://en.wikipedia.org/wiki/Great-circle_distance))

The corresponding jupyter notebook: [jupyter/city_distances.ipynb](https://github.com/thxi/dsba/blob/master/jupyter/city_distances.ipynb)

---
At this point there were 2 datasets:
[data/ru_dist_mat_v1.csv](https://github.com/thxi/dsba/blob/master/data/ru_dist_mat_v1.csv)
and
[data/ru_dist_mat_v2.csv](https://github.com/thxi/dsba/blob/master/data/ru_dist_mat_v2.csv)

postfix:
* v1 - Including all russian cities
* v2 - Including only russian cities with population > 200k

To see how the second one was obtained see [jupyter/Big cities.ipynb](https://github.com/thxi/dsba/blob/master/jupyter/Big%20cities.ipynb)

---

Algorithms can be found in [algs](https://github.com/thxi/dsba/tree/master/algs) directory;
* [boruvka.py](https://github.com/thxi/dsba/blob/master/algs/boruvka.py)
* [kruskal.py](https://github.com/thxi/dsba/blob/master/algs/kruskal.py)
* [prim.py](https://github.com/thxi/dsba/blob/master/algs/prim.py)

To get the MSTs run:
```bash
python3 algs/mst.py v* # where * is either 1 or 2
```



---

Distances between roads were acquired with the use of [Google Distance Matrix](https://developers.google.com/maps/documentation/distance-matrix/intro)

Corresponding [jupyter notebook](https://github.com/thxi/dsba/blob/master/jupyter/Google%20Distance%20Matrix.ipynb)

Corresponding [dataset v1](https://github.com/thxi/dsba/blob/master/data/mst_real_edges_small.csv) [dataset v2](https://github.com/thxi/dsba/blob/master/data/mst_real_edges_big.csv)

---

The obtained MSTs were visualized using Folium library
[algs/html_maps.py](https://github.com/thxi/dsba/blob/master/algs/html_maps.py)
```bash
python3 algs/html_maps.py v* # where * is either 1 or 2
```

Or refer to [jupyter/Comparing distances.ipynb](https://github.com/thxi/dsba/blob/master/jupyter/Comparing%20distances.ipynb) where we made the interactive maps (maps/comparison_map_markers_v* or maps/comparison_map_* or better use the web app)


Used resources:
---


[cities dataset](https://github.com/datasets/world-cities?files=1)

[yandex geocoder](https://tech.yandex.com/maps/jsapi/doc/2.1/quick-start/index-docpage/)

[Google Distance Matrix](https://developers.google.com/maps/documentation/distance-matrix/intro)

[heroku](https://www.heroku.com/) to deploy the visualized data