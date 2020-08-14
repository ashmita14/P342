// Question 1b : We consider a 6 cross 6 grid

#include<iostream>
#include<cstdlib>
using namespace std;

int main(){
	//declaring variables
	int i,j, k, l;
	int N, NN;
	int totp;
	int totdis=0;
	double avgdis;
	
	//total number of points in a row
	N=6;
	//total number of points
	NN=N*N;
	//total number of pairs possible
	totp=NN*NN;
	
	//first two loops choose first point on the grid
	for(i=0;i<N;i++){
		for(j=0;j<N;j++){
			//second two loops traverse the entire grid and choose the second point
			for(k=0;k<N;k++){
				for(l=0;l<N;l++){
					totdis=totdis+abs(i-k)+abs(j-l);
				}
			}
		}
	}
	avgdis=double(totdis)/double(totp);
	cout<<"Number of points in "<<N<<"x"<<N<<" grid = "<<NN<<endl;
	cout<<"Number of pairs possible = " <<totp<<endl;
	cout<<"Total distance = "<<totdis<<endl;
	cout<<"Average distance = "<<avgdis<<endl;
}
	
