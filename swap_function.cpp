#include<iostream>
using namespace std;
void swap(int *a,int *b){int temp=*a;
                            *a=*b;
                            *b=temp;}
 int main(){
    int a=5;
    int b=7;
    int *x=&a;
    int *y=&b;
    swap(*x,*y);
   cout<<"a= "<<a<<"b= "<<b<<endl;
    return 0;
 }