#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    string words[N];
    
    for (int i = 0; i < N; i++){
        cin >> words[i];
    }

    sort(words, words+N);

    for (int i = 0; i < N; i++){
        cout << words[i] << '\n';
    }

    return 0;
}