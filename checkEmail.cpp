// This file is checking whether the email input is correct
// or not , incase of incorrectness it will , again ask for
// the email .

#include <iostream>
#include <regex>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    string str;
    const regex pattern("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+");

    while (true)
    {
        cout << "Enter your Email-Id:" << endl;
        cin >> str;

        if (regex_match(str, pattern))
        {

            fstream file;

            file.open("checkEmail.txt", ios::out);
            file << str;
            file.close();

            break;
        }
    }

    return 0;
}