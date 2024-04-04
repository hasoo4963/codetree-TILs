#include <iostream>
using namespace std;

bool isPrime(int a){
    if (a == 1){
        return false;
    }
    if (a == 2){
        return true;
    }

    for (int i = 2; i < a; i++){
        if (a % i == 0){
            return false;
        }
    }
    return true;
}

bool isEven(int a){
    int sum = 0;
    while(a){
        sum += a%10;
        a /= 10;
    }

    if(sum % 2 == 0){
        return true;
    }
    else {
        return false;
    }
}

void countAndPrintNum(int a, int b){
    int count = 0;
    for (int i = a; i <= b; i++){
        if(isPrime(i) && isEven(i)){
            count++;
        }
    }
    cout << count << endl;
}

int main() {
    // 여기에 코드를 작성해주세요.

    int a, b;
    cin >> a >> b;

    countAndPrintNum(a, b);

    return 0;
}