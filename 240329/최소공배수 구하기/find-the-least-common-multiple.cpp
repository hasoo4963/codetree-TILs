#include <iostream>
using namespace std;


int GCD(int n, int m){
    int c;
    while(m != 0){
        c = n % m;
        n = m;
        m = c;
    }
    return n;
}

void LCD(int n, int m, int gcd){
    cout << (n*m)/gcd;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n, m;
    cin >> n >> m;

    int gcd = GCD(n,m);
    LCD(n,m,gcd);

    return 0;
}