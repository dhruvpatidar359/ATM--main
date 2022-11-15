#include<iostream>
using namespace std;

long long int aadharCheck(){
    long long int aadharNumber;
    cout << "Enter Your aadhar Number ";
    cin >> aadharNumber;

    if(to_string(aadharNumber).length() == 12){
        
        return aadharNumber;
        
    }
    cout<<"invalid aadhar number\n";

    aadharCheck();
    return 0;
}

int main(){
     return aadharCheck();
}