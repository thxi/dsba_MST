#include<iostream>

int main (void)
{
    int a, b, u, v, n, i, j, z = 1;
    int visited[10] = {0}, min, mincost = 0, cost[10][10];
    int path[100] = {0};
    //В этот массив будут записываться вершины, по которым составится путь
    int path_index = 0;

    //clrscr();
    //Функция clrscr() полностью очищает активное текстовое окно и помещает курсор в левый верх­ний угол (1,1).
    std::cout << "Number of vertices  ";
    std::cin >> n;
    std::cout << "Adjacency matrix\n";

    for (i = 1; i <= n; i++)
        for (j = 1;j <= n; j++)
        {
            std::cin >> cost[i][j];
            if (cost[i][j] == 0)
                cost[i][j] = 999;
            //999 - это что-то типа бесконечности. Должно быть больше чем значения веса каждого из ребер в графе
        }
    visited[1] = 1;
    std::cout << "\n";

    while(z < n)
    {
        for (i = 1, min = 999; i <= n; i++)
            for (j = 1; j <= n; j++)
                if (cost[i][j] < min)
                    if (visited[i] != 0)
                    {
                        min = cost[i][j];
                        a = u = i;
                        b = v = j;
                    }
        if (visited[u] == 0 || visited[v] == 0)
        {
            path[path_index] = b;
            path_index++;
            //cout <<"\n "<< z++ <<"  "<<a<<"  "<< b << min; //Можно вывести так
            z++;
            mincost += min;
            visited[b] = 1;

        }
        cost[a][b]=cost[b][a] = 999;
    }


    std::cout<< "\n";

    std::cout<< 1 << " --> ";
    for (int i = 0; i < n - 1; i++)
    {
        std::cout << path[i];
        if (i < n - 2)
            std::cout << " --> ";
    }

    std::cout << "\n Minimal weight  " << mincost;


    std::cin.get();
    std::cin.get();
}
