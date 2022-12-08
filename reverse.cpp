#include<iostream>
using namespace std;
int reverse(int a){
     int rev=0;
    while(a>=1){  rev=rev*10+a%10;
    a=a/10;
      }
     return rev;
}
int main(){
    int n;
    cin>>n;
   
    cout<<reverse(n)<<endl;


    return 0;
}
