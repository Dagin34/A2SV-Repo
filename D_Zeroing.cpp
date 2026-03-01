#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int arr_size, ops;
    cin >> arr_size >> ops;

    vector<int> arr(arr_size);
    for (int i = 0; i < arr_size; i++){
        cin >> arr[i];
    }

    set<int> unique_arr;
    for (int n : arr){
        if (n != 0){
            unique_arr.insert(n);
        }
    }

    int subs = 0;
    int count = 0;

    vector<int> filtered(unique_arr.begin(), unique_arr.end());
    for (int num : filtered){
        if (count >= ops) break;

        int diff = num - subs;
        cout << diff << "\n";

        subs = num;
        count++;
    }

    while (count < ops){
        cout << 0 << '\n';
        count++;
    }

    return 0;
}