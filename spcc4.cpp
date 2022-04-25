#include <iostream>
using namespace std;
int main()
{
  int i=0 , state=0, flag=0; char s[100];
  cin>>s;
  while(s[i] !='\0')
  {
    switch(state){
      case 0: if(s[i]=='<') state=1;
              else if(s[i]=='>') state=5;
              else if(s[i]== '=') state=4;
              else state= 3;
              break;
      case 1: if(s[i] == '=') state=2;
              else if(s[i]=='>') state=9;
              break;
      case 5: if(s[i] == '=') state=6;
              else state=7;
              break;
      case 4: if(s[i]=='=')   state=8;
              break;
    }
    i++;
  }
  if(state==1) cout<<"L";
  if(state==2) cout<<"LE";
  if(state==3 || state==7) cout<<"Invalid";
  if(state==6) cout<<"GE";
  if(state==5) cout<<"G";
  if(state==8) cout<<"E";
  if(state==9)
  cout<<"NT";
   cout<<endl;
  return 0;
}