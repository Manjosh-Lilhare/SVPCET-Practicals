#include <iostream>
#include <vector>
using namespace std;
#define vi vector<int>
#define vvi vector<vi>
#define pii pair<int, int>
#define vii vector<pii>
#define rep(i, a, b) for (int i = a; (i < b); i++)
#define ff first
#define ss second
#define setbits(x) builtin_popcount(x)
const int N = 1e5 + 2, MOD = 1e9 + 7;
// class graph{
// public:
// vector<vector<int>> adjm(n+1,vector<int>ex(n+1,0));
// };
int DFT(){
    // Code of Depth First Traversal
}
int BFT(){
    // Code of Breadth First Traversal
}
signed main()
{
    int n, m, z; // here {n} is number of nodes and {m} is nuuumber of edges
    cout << "Enter number of Nodes and Edges respectively" << endl;
    cin >> n >> m;
    // Code of adjecency matrix start
    vvi adjm(n + 1, vi(n + 1, 0));
    // cout<<"Now enter the Edges"<<endl;
    cout << "Enter your type" << endl
         << "1.For directed graph" << endl
         << "2.For undirected graph";
    cin >> z;
    if (z == 1)
    {
        rep(i, 0, m)
        {
            int x, y;
            cout << "Enter Edge" << endl;
            cin >> x >> y;
            cout << endl;
            adjm[x][y] = 1;
        }
    }
    else if (z == 0)
    {
        rep(i, 0, m)
        {
            int x, y;
            cout << "Enter Edge" << endl;
            cin >> x >> y;
            cout << endl;
            adjm[x][y] = 1;
            adjm[y][x] = 1;
        }
    }
    else
    {
        cout << "Invalid entry";
    }
    cout << "Your adjecency Matrix is given as:" << endl;
    if (z == 1)
    {

        cout << "Your directed graph is:";
        rep(i, 0, n + 1)
        {
            rep(j, 1, n + 1)
            {
                cout << adjm[i][j] << " ";
            }
            cout << endl;
        }
    }
    else
    {
        cout << "Your Undirected graph is:";
        rep(i, 0, n + 1)
        {
            rep(j, 1, n + 1)
            {
                cout << adjm[i][j] << " ";
            }
            cout << endl;
        }
    }
    // Code of adjecency matrix end
    // Code of adjecency list start

    // vi adjl(n+1);
    // cout << "Enter your type" << endl
    //      << "1.For directed graph" << endl
    //      << "2.For undirected graph";
    // cin >> z;
    // if (z == 1)
    // {
    //     rep(i, 0, m)
    //     {
    //         int x, y;
    //         cout << "Enter Edge" << endl;
    //         cin >> x >> y;
    //         cout << endl;
    //         adjm[x].push_back(y);
    //     }
    // }
    // else if (z == 0)
    // {
    //     rep(i, 0, m)
    //     {
    //         int x, y;
    //         cout << "Enter Edge" << endl;
    //         cin >> x >> y;
    //         cout << endl;
    //         adjm[x].push_back(y);
    //         adjm[y].push_back(x);
    //     }
    // }
    // else
    // {
    //     cout << "Invalid entry";
    // }
    // cout << "Your adjecency Matrix is given as:" << endl;
    // if (z == 1)
    // {

    //     cout << "Your directed graph is:";
    //     rep(i, 0, n + 1)
    //     {
    //         cout << i << "->";
    //         for (int x : adjl[i].std::begin())
    //         {
    //             cout << x << " ";
    //         }
    //         cout << endl;
    //     }
    // }
    // else
    // {
    //     cout << "Your Undirected graph is:";
    //     rep(i, 0, n + 1)
    //     {
    //         cout << i << "->";
    //         for (int x : adjl[i])
    //         {
    //             cout << x << " ";
    //         }
    //         cout << endl;
    //     }
    // }

    // Code of adjecency list end

    return 0;
}