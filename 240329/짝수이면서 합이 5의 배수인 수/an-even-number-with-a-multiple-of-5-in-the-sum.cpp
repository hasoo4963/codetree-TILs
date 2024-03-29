#include <iostream>
using namespace std;

bool isSum5(int);

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;

        if(isSum5(n) && (n % 2 == 0)){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl; 
        }

    return 0;
}

bool isSum5(int n){
    int result = (n/10) + (n%10);
    if (result % 5 == 0){
        return true;
    }
    else {
        return false;
    }
}