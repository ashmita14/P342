// Question 1a N=6: o--o--o--o--o--o

#include<iostream>
#include<cstdlib>
using namespace std;

int main(){
	//declaring variables
	int i,j;
	int N;
	int totp;
	int totdis=0;
	double avgdis;
	
	//total number of points
	N=6;
	//number of ways a pair can be chosen
	totp=N*N;
	
	//first loop chooses the first point
	for(i=0;i<N;i++){
		//second loop chooses the second point
		for(j=0;j<N;j++){
			totdis=totdis+abs(i-j);
		}
	}
	avgdis=double(totdis)/double(totp);
	cout<<"Number of points in a line = "<<N<<endl;
	cout<<"Total number of pairs possible = "<<totp<<endl;
	cout<<"Total distance = "<<totdis<<endl;
	cout<<"Average Distance = "<< avgdis<<endl;
}
