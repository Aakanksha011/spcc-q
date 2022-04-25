#include<stdio.h>
int main()
{
    int i=0 , state=0;
    char s[100];
    gets(s);
    while(s[i] !='\0')
          {
    switch(state){
            case 0: if(s[i]=='a') state=1;
                    else if(s[i]=='b') state=2;
                    else state=0;
	break;

            case 1: if(s[i]=='a') state=1;
                    else if(s[i]=='b') state=2;
                    else state=0;
   	break;

            case 2: if(s[i]=='a') state=3;
                    else if(s[i]=='b') state=2;
                    else state=0;
  	break;

            case 3: if(s[i]=='a') state=1;
                    else if(s[i]=='b') state=4;
                    else state=0;
  	break;

            case 4: if(s[i]=='a') state=4;
                    else if(s[i]=='b') state=4;
                    else state=0;
  	break;
          }
          i++;
      }
   if(state==4)
     printf("Accepted");
   else
     printf("Rejected");
   return 0;
 }
