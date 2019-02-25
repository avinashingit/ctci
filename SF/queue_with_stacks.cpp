/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-25T17:12:53-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Practice
 * @Filename: queue_with_stacks.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-25T17:22:11-06:00
 * @License: MIT License
 */

#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s, t;
    int operation = 0;
    int number;
    while(operation != -1) {
        cout<<"Enter the operation \n 1. Push \n 2. Pop"<<endl;
        cin>>operation;
        if(operation == -1) break;
        if(operation == 1) {
            cout<<"Enter the number to be pushed"<<endl;
            cin>>number;
            s.push(number);
        }
        else if(operation == 2) {
            if(t.empty()) {
                while(!s.empty()) {
                    int x = s.top();
                    s.pop();
                    t.push(x);
                }
            }
            if(t.empty()) {
                cout<<"Nothing to be popped. Please push"<<endl;
            }
            else {
                int top = t.top();
                t.pop();
                cout<<"The popped element is "<<top<<endl;
            }
        }
    }
}
