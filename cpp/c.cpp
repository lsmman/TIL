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
2 # T
2 2  # N K #1
1 2 # 칼로리_A[i] #1
4 2 # 칼로리_B[i] #1
3 2 # N K #2
6 3 1 # 칼로리_A[i] #2
1 4 3 # 칼로리_B[i] #2

output
Case #1
5
Case #2
4
**/