#include <iostream>
#include <set>

using namespace std;

#define MAX_NODES 100 

void DFS(int node, int adjm[MAX_NODES][MAX_NODES], bool visited[MAX_NODES], set<int>& component, int n) {
    visited[node] = true;
    component.insert(node);

    for (int i = 1; i <= n; i++) {
        if (adjm[node][i] == 1 && !visited[i]) {
            DFS(i, adjm, visited, component, n);
        }
    }
}

void getConnectedComponents(int adjm[MAX_NODES][MAX_NODES], int n) {
    bool visited[MAX_NODES] = {false};
    int componentCount = 0;

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            set<int> component;
            DFS(i, adjm, visited, component, n);
            componentCount++;
            cout << "Component " << componentCount << ": ";
            for (int node : component) {
                cout << node << " ";
            }
            cout << endl;
        }
    }
}

int main() {
    int n, m, z;
    cout << "Enter number of Nodes and Edges respectively: ";
    cin >> n >> m;

    int adjm[MAX_NODES][MAX_NODES] = {0};

    cout << "Enter type (1 for Directed, 0 for Undirected): ";
    cin >> z;

    for (int i = 0; i < m; i++) {
        int x, y;
        cout << "Enter Edge: ";
        cin >> x >> y;
        adjm[x][y] = 1;
        if (z == 0) adjm[y][x] = 1;
    }

    cout << "Your Adjacency Matrix:\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adjm[i][j] << " ";
        }
        cout << endl;
    }

    cout << "Connected Components:\n";
    getConnectedComponents(adjm, n);
    
    return 0;
}

