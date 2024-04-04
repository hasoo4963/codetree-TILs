#include <iostream>
using namespace std;

bool isContinue(int n1, int n2, int *arr1, int *arr2){
    for (int i = 0; i < n2; i++){ //arr2
        for (int x = 0; x < n1; x++){   //arr1
            if(arr1[x] == arr2[i]){
                int tempArr2Idx = i + 1;
                int tempArr1Idx = x + 1;

                if(arr1[tempArr1Idx] == arr2[tempArr2Idx]){
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n1, n2;
    cin >> n1 >> n2;

    int arr1[n1] = {0};
    int arr2[n2] = {0};

    int temp;
    for (int i = 0; i < n1; i++){
        cin >> temp;
        arr1[i] = temp;
    }

    for (int i = 0; i < n2; i++){
        cin >> temp;
        arr2[i] = temp;
    }

    if(isContinue(n1, n2, arr1, arr2)){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}