// problem 1

// g++ c.cpp -o c; ./c

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int Answer;

int main(int argc, char** argv)
{
    int T, test_case;
    freopen("input.txt", "r", stdin);

    cin >> T;
    for (test_case = 0; test_case < T; test_case++)
    {
        // Define
        int n, k;
        vector<int> a, b;
        int max_val;
        Answer = 0;

        // Read input & assign var
        cin >> n >> k;
        for (int i=0; i < n; i++){
            int x;
            cin >> x;
            a.push_back(x);
        }
        for (int i=0; i < n; i++){
            int x;
            cin >> x;
            b.push_back(x);
        }
        // sort each vector (a, b)
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        cout << "Case #" << test_case+1 << endl;
        cout << Answer << endl;
    }
    return 0;
}

/**
 * 1<=T<=100
 * 1<=N<=200,000
 * 1<=K<=N
 * 칼로리 값은 10^9이하
 * 
input
- N은 세로선 개수, k는 가로 이음선 개수, m의 출발점과 도착점의 쌍의 개수

3 # T
3 4 4 # N, k, m
1 2 # k1
2 3 # k2
1 2 # k3
1 3 # k4
1 1 # m1
1 2 # m2
2 3 # m3
3 2 # m4
output
Case #1
3
Case #2
6
Case #3
1
**/