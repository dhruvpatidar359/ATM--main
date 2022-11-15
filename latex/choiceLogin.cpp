#include <iostream>
using namespace std;

int afterLogin()
{
    int choice;
    cin >> choice;
    if (choice > 0 && choice < 4)
    {
        return choice;
    }
    printf("invalid choice\n");
    afterLogin();
    return 0;
}

int main()
{

    return afterLogin();
}
