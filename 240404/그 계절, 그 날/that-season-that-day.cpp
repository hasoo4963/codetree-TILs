#include <iostream>
using namespace std;

bool isLeapYear(int year){
    if (year % 4 != 0){
        return false;
    }

    if (year % 100 != 0){
        return true;
    }

    if (year % 400 == 0){
        return true;
    }

    return false;
}

bool isAvailable(int year, int month, int day){

    int datArray[13] = {0,1,0,1,0,1,0,1,1,0,1,0,1};

    if(isLeapYear(year)){
        if(month == 2){
            if(day <= 29){
                return true;
            } else {
                return false;
            }
        } else {
            if(datArray[month] == 1 && day <= 31){
                return true;
            } else if (datArray[month] == 0 && day <= 30){
                return true;
            } else {
                return false;
            }
        }
    }
    else {
        if (month == 2 && day <= 28){
            return true;
        } else if (month == 2 && day > 28){
            return false;
        } else if(datArray[month] == 1 && day <= 31){
            return true;
        } else if (datArray[month] == 0 && day <= 30){
            return true;
        } else {
            return false;
        }
    }
}

void whatSeason(int year, int month, int day){
    if(month >= 3 && month <= 5){
        cout << "Spring" << endl;
    } else if (month >= 6 && month <= 8){
        cout << "Summer" << endl;
    } else if (month >= 9 && month <= 11){
        cout << "Fall" << endl;
    } else {
        cout << "Winter" << endl;
    }
}

void printSeason(int year, int month, int day){
    if(isAvailable(year,month,day)){
        whatSeason(year,month,day);
    }
    else {
        cout << -1 << endl;
    }
}

int main() {
    // 여기에 코드를 작성해주세요.

    int year, month, day;
    cin >> year >> month >> day;

    printSeason(year, month, day);

    return 0;
}