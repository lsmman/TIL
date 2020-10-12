#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int T, testCase;
    cin >> T;
    for (testCase = 1; testCase <= T; testCase++) {
        int n, k;
        cin >> n >> k;
        vector<int> a;
        for (int i=0; i < n; i++){
            int x;
            cin >> x;
            a.push_back(x);
        }
        sort(a.begin(), a.end());
        int result = 1;
        for(int i=1; i<n; i++){
            if (a[i] - a[i - result] <= k) result++;
        }
        cout << "Case #" << testCase << '\n';
        cout << result << '\n';
    }
    return 0;
}