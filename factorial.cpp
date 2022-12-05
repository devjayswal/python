#include<iostream>
using namespace std;

int fact(int a){
    int fact=1;
    while(a>1){fact=fact*a;
    a--;}
        return fact;
    }

void evenodd(int b){ if(b%2==0){cout<<b<<endl;}
                     else{cout<<"odd"<<endl;}
                     return ;}

int main(){ int n;
                cout<<"plese enter a number"<<endl;
                cin>>n;
                int m=fact(n);
                evenodd(m);
                return 0;}                     