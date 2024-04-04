#include <iostream>
using namespace std;

bool isComplete(int a){
    if (a % 2 == 0){
        return false;
    }

    if (a % 10 == 5){
        return false;
    }

    if (a % 3 == 0 && a % 9 != 0){
        return false;
    }

    return true;
}

void countAndPrintCmpNum(int a, int b){
    int count = 0;
    for (int i = a; i <= b; i++){
        if(isComplete(i)){
            count++;
        }
    }
    cout << count << "\n";
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    countAndPrintCmpNum(a, b);
    return 0;
}