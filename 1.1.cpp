/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-25T15:28:37-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: CTCI
 * @Filename: 1.1.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-25T15:33:16-06:00
 * @License: MIT License
 */



#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

bool has_unique_characters(string s) {
    map<char, int> m;
    for(int i=0;i<s.size();i++) {
        if(m.find(s[i]) != m.end()) {
            m[s[i]] += 1;
            return false;
        }
        else {
            m[s[i]] = 1;
        }
    }
    return true;
}

bool has_unique_characters_method2(string s) {
    sort(s.begin(), s.end());
    for(int i=1;i<s.length();i++) {
        if(s[i] == s[i-1]) {
            return false;
        }
    }
    return true;
}

int main() {
    string str;
    cin>>str;
    cout<<has_unique_characters(str)<<endl;
    cout<<has_unique_characters_method2(str)<<endl;
    return 0;
}
