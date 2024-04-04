#include <iostream>
using namespace std;

void printResult(int a, char b, int c){
    switch(b){
    case '+':
        cout << a << " + " << c << " = " << a+c << endl;
        break;
    case '-':
        cout << a << " - " << c << " = " << a-c << endl;
        break;
    case '/':
        cout << a << " / " << c << " = " << a/c << endl;
        break;
    case '*':
        cout << a << " * " << c << " = " << a*c << endl;
        break;
    default:
        cout << "False" << endl;
        return;
    }
}

int main() {
    // 여기에 코드를 작성해주세요.

    int a, c;
    char b;

    cin >> a >> b >> c;

    printResult(a,b,c); 

    return 0;
}