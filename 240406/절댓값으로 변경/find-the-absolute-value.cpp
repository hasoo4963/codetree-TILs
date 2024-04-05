#include <iostream>
using namespace std;

void printArr(int* arr, int n){
    for (int i = 0; i < n; i++){
        if (arr[i] < 0){
            cout << -1*arr[i] << " ";
        } else {
            cout << arr[i] << " ";
        }
    }
    cout << "\n";
}

int main() {
    int n, temp;
    cin >> n;

    int arr[n] = {0};
    for (int i = 0; i < n; i++){
        cin >> temp;
        arr[i] = temp;
    }

    printArr(arr, n);

    return 0;
}