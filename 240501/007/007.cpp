#include <iostream>
#include <string>
using namespace std;

class Object {
    public:
        string secret_code, meeting_point;
        int time;

        Object(string code, string point, int time) {
            this->secret_code = code;
            this->meeting_point = point;
            this->time = time;
        }
};

int main() {
    string code, point;
    int time;

    cin >> code >> point >> time;

    Object obj1 = Object(code, point, time);
    cout << "secret code : " << obj1.secret_code << "\n";
    cout << "meeting point : " << obj1.meeting_point << "\n";
    cout << "time : " << obj1.time << "\n";
    return 0;
}