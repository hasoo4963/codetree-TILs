#include <iostream>
using namespace std;

int sumAndDivide(int);

int main() {
    // 여기에 코드를 작성해주세요.
    int N;
    cin >> N;

    cout << sumAndDivide(N);

    return 0;
}

int sumAndDivide(int N){
    int sum = 0;
    for (int i = 1; i <= N; i++){
        sum += i;
    }
    return sum/10;
}