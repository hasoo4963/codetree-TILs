#include <iostream>
using namespace std;

bool isInclude(int i){
    int divide = 10;

    // 1의 자리 숫자 확인
    if (i % 10 == 3){
        return true;
    }
    else if (i % 10 == 6){
        return true;
    }
    else if (i % 10 == 9){
        return true;
    }

    // 10의 자리부터 끝자리 숫자 (최대 1,000,000)까지 확인
    for (int x = 0; x < 5; x++){
        if(i/divide == 3){
            return true;
        }
        else if (i/divide == 6){
            return true;
        }
        else if (i/divide == 9){
            return true;
        }
        else{
            divide *= 10;
        }
    }

    //수 전체에 3 또는 6 또는 9가 하나도 없으로 false return
    return false;
}

bool isDivide3(int i){
    //3의 배수인지 확인하고 알맞은 값 return
    if (i % 3 == 0){
        return true;
    }
    else {
        return false;
    }
}

bool isMagicNumber(int i){
    if(isInclude(i) || isDivide3(i)){
        return true;
    }
    else {
        return false;
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    int count = 0;
    for (int i = a; i <= b; i++){
        if(isMagicNumber(i)){
            count++;
        }
    }
    cout << count << endl;
    return 0;
}