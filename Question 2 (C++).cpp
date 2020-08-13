//Question 2

#include<iostream>
using namespace std;

int main(){
//declaring vectors
int A[3]={3,8,7};
int B[3]={5,2,9};

//declaring variables
int S[3];
int i, D=0;

//calculating sum and dot product
for(i=0;i<3;i++){
S[i]=A[i]+B[i];  //A+B (sum)
D=D+A[i]*B[i];   // A>B (dot product)
}

//printing results
cout<<"Vector A : [" ;
for(i=0;i<3;i++) cout<<A[i] << " ";
cout<<"]"<<endl;
cout<<"Vector B : [";
for(i=0;i<3;i++) cout<<B[i] << " ";
cout<<"]"<<endl;
cout<<"Sum of A and B : [";
for(i=0;i<3;i++) cout<<S[i] << " ";
cout<<"]"<<endl;
cout<<"Dot product of A and B = "<<D << endl;

return 0;
}



/* OUTPUT (directly copy pasted from run window 
Vector A : [3 8 7 ]
Vector B : [5 2 9 ]
Sum of A and B : [8 10 16 ]
*/
