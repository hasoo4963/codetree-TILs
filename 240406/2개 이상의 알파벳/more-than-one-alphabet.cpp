#include <iostream>
#include <string>
using namespace std;

bool isThereUp2(string a){
    int length = a.length();
    char init;

    for (int i = 0; i < length; i++){
        init = a[i];
        for (int x = 1; x < length; x++){
            if (a[x] == init){
                return true;
            }
        }
    }
    return false;
}

int main() {
    // 여기에 코드를 작성해주세요.
    string a;
    cin >> a;

    if (isThereUp2(a)){
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}