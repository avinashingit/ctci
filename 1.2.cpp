/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-25T15:40:32-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: CTCI
 * @Filename: 1.2.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-25T15:56:20-06:00
 * @License: MIT License
 */

 #include <iostream>
 #include <vector>
 #include <string>
 #include <map>
 #include <algorithm>

 using namespace std;

bool check_anagram(string s1, string s2) {
    if(s1.length() != s2.length()) {
        return false;
    }
    map<char, int> m1, m2;
    for(int i=0;i<s1.length();i++) {
        m1[s1[i]] += 1;
        m2[s2[i]] += 1;
    }
    for(auto it = m1.begin();it != m1.end();it++) {
        if(m2[it->first] != it->second) {
            return false;
        }
    }
    return true;
}

bool check_anagram_method2(string s1, string s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return s1 == s2;
}

 int main() {
     string str1, str2;
     cin>>str1>>str2;
     cout<<check_anagram(str1, str2)<<endl;
     cout<<check_anagram_method2(str1, str2)<<endl;
     return 0;
 }
