#include <iostream>
#include <string>
using namespace std;

bool isPalin(string &a){
    int length = a.length();
    for (int i = 0; i < a.length(); i++){
        length--;
        if(a[i] != a[length]){
            return false;
        }
    }
    return true;
}

int main() {
    // 여기에 코드를 작성해주세요.
    string a;
    cin >> a;

    if(isPalin(a)){
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}