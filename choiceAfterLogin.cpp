//  This file is taking the choice from the user and transfering it into python

#include <iostream>
using namespace std;

int afterLogin()
{

    int choice;
    cout << "Enter the Choice :";
    cin >> choice;
    if (choice > 0 && choice < 7)
    {
        return choice;
    }
    cout << "invalid choice\n";

    afterLogin();

    return 0;
}

int main()
{

    return afterLogin();
}
