#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{

    long long int aadharNumber;
    while (true)
    {

        cout << "Enter Your aadhar Number ";
        cin >> aadharNumber;

        if (to_string(aadharNumber).length() == 12)
        {

            fstream file;

            // opening file "Gfg.txt"
            // in out(write) mode
            // ios::out Open for output operations.
            file.open("checkAadhar.txt", ios::out);
            file << to_string(aadharNumber);
            file.close();
            break;
        }
    }

    return 0;
}