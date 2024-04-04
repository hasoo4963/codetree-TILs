#include <iostream>
using namespace std;

bool isAvailable(int month, int day){

    // 1 -> 31            0 -> 30
    int datArray[13] = {0,1,0,1,0,1,0,1,1,0,1,0,1};

    if(month == 2 && day <= 28){
        return true;
    }

    if(month == 2 && day > 28){
        return false;
    }

    if(datArray[month] == 1 && day <= 31){
        return true;
    } else if (datArray[month] == 0 && day <= 30){
        return true;
    } else{
        return false;
    }

}

int main() {
    // 여기에 코드를 작성해주세요.
    int month, day;
    cin >> month >> day;

    if(isAvailable(month, day)){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}