#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 1, b = 2, c = 3;
    int tempSum = a + b + c;
    a = tempSum;
    b = tempSum;
    c = tempSum;
    cout << a << " " << b << " " << c;
    return 0;
}