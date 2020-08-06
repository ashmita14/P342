//Question 2

#include<iostream>
using namespace std;

int main(){
int i, n;
int fac =1;
cout<<"Enter n"<< endl;
cin>>n;
if(n>=0){
for(i=n;i>=1;i--) fac=fac*i;
cout<<"Factorial of "<< n <<" = "<< fac <<endl;
}
else cout<< n << " is a negative nunber." << endl;
}
