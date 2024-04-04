#include <iostream>
using namespace std;

void modify(int *arr, int n){
    for (int i = 0; i < n; i++){
        if(arr[i] % 2 == 0){
            arr[i] /= 2;
        }
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n, temp;
    cin >> n;
    int arr[n] = {0};
    for (int i = 0; i < n; i++){
        cin >> temp;
        arr[i] = temp;
    }

    modify(arr, n);

    for (int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
    cout << "\n";
    return 0;
}