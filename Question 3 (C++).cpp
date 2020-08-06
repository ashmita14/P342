// Question 3

#include<iostream>
using namespace std;

int main(){
int i,n;
double nn,sum=0.0, diff;
cout<<"Enter n"<<endl;
cin>>n;
for(i=1;i<=n;i++){
diff=sum;
nn=double(i);
sum=sum+1.0/nn ;
diff=sum-diff;
if(diff<=0.001){
cout<< "Sum does not change by more than 0.001"<< endl;
break;
}
}
cout<<"Sum = "<< sum <<endl;
}
