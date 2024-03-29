#include <iostream>
using namespace std;

int min(int,int,int);

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c;
    cin >> a >> b >> c;

    cout << min(a,b,c) << endl;

    return 0;
}

int min(int a, int b, int c){
    int array[3] = {a,b,c};
    int min = array[0];

    for(int i = 0; i < 3; i++){
        if(min > array[i]){
            min = array[i];
        }
    }
    return min;
}