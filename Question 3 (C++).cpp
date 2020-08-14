// Question 3

#include<iostream>
#include<fstream> // to read/write to/from files
#include<string>
#include<cstdlib>
using namespace std;

int main(){
//declaring variables and arrays
int i,j, k, term;
int M[3][3];int N[3][3];
int A[3]={3,8,7}; //same as question 2
int MA[3]={0,0,0};
int MN[3][3]={{0,0,0},{0,0,0},{0,0,0}};
string s; 
string delim= ",";
string val;
int pos=0;

//resetting values of i and j
i=0;j=0;
ifstream f;
ifstream g;
f.open("M.txt");
g.open("N.txt");
if(!f) cout<<"File containing Matrix M not opened."<<endl;
else if(!g) cout <<"File containing Matrix N not opened"<<endl;
else{ 
	//running loop until end of each file is reached
	while(f.eof()!=true){
		j=0; 							//resetting j at the begnning of every loop
		f>>s; 							//storing the lines in a string
		//extracting term by term from the line with delimiter ','
		while(j<3){
			pos=s.find(delim); 			//finding position of delimiter
			if(j!=2) val=s.substr(0,pos); 
			if(j==2) val=s; //last value with no demilimter after it
			//converting to integer and storing in matrix M
			M[i][j]=stoi(val);
			//erasing string upto the extracted value
			s.erase(0,pos+delim.length());
			j++; 				//incrementing j
		}
		i++; 					//incrementing i
	}
	val=""; 					//resetting val
	i=0; j=0; 					//resetting i and j
	//repeating same procedure for file g and Matrix N
	while(g.eof()!=true){
		j=0;
		g>>s;
		while(j<3){
			pos=s.find(delim);
			if(j!=2) val=s.substr(0,pos);
			if(j==2) val=s;
			N[i][j]=stoi(val);
			s.erase(0,pos+delim.length());
			j++;
		}
		i++;
	}
}
//finding M cross A
for(i=0;i<3;i++){
	for(j=0;j<3;j++){
		term=MA[i];
		MA[i]=term+M[i][j]*A[j];
	}
}
//finding M cross N
for(i=0;i<3;i++){
	for(j=0;j<3;j++){
		for(k=0;k<3;k++){
			term=MN[i][j];
			MN[i][j]=term+M[i][k]*N[k][j];
		}
	}
}
//Printing Matrices

//Matrix M
cout<<" Matrix M : "<< endl;
for(i=0;i<3;i++){
	for(j=0;j<3;j++) {
		cout<<"\t"<<M[i][j]<<"\t";
	}
	cout<<endl;
}

//Matrix N
cout<<" Matrix N : " << endl;
for(i=0;i<3;i++){
	for(j=0;j<3;j++){
		cout<<"\t"<<N[i][j]<<"\t";
	}
	cout<<endl;
}

//M cross A
cout<<" Matrix MxA : " <<endl;
for(i=0;i<3;i++){
	cout<<"\t"<<MA[i]<<endl;
}

//M cross N
cout<<" Matrix MxN : "<<endl;
for(i=0;i<3;i++){
	for(j=0;j<3;j++){
		cout<<"\t"<<MN[i][j]<<"\t";
	}
	cout<<endl;
}
}
