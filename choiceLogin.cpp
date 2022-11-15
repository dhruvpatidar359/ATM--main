#include<iostream>
using namespace std;

int login()
{
    int choice;
    cin>>choice;
    if (choice > 0 && choice < 4)
    {
        return choice;
    }
    printf("invalid choice\n");
    login();
    return 0;
}

int main()
{

    return login();
}
