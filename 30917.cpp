#include <iostream>
using namespace std;
int main() {
    int respA;
    for(int a=1; a<=9; a++){
        // A가 a인지 물어보고 flush를 한다.
        // endl은 자동으로 flush도 해준다.
        cout << "? A " << a << endl;

        // 채점기의 답변을 입력받는다.
        cin >> respA;

        if(respA == 1){
            // 답변이 "예"이므로 A의 값은 a이다.
            // B의 값도 알아내야 하는데, 이 부분은 직접 채워보자.
            int b;
            int respB;
            for(b=1; b<=9; b++){
                cout << "? B " << b << endl;

                // 채점기의 답변을 입력받는다.
                cin >> respB;
                if( respB == 1 ){
                    cout << "! " << a + b;
                    break;
                }
            }
            break;
        }
    }
}