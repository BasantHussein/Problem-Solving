#include <iostream>
#include <string>
#include<string>
using namespace std;

int main()
{
    string s;
    string t;
    cin>>s>>t;
    int h1,h2,m1,m2,h,m;
    if(int(s[0])==0 && int(s[1])==0)
    {
        s[0]='2';
        s[1]='4';
       if(int(t[0])==0 && int(t[1])==0)
       {
           t[0]='2';
           t[1]='4';
       }
       h= s[0:2]-t[0:2];
       //h1=int(s[0]-t[0]);
      // h2=int(s[1]-t[1]);
       m= s[3:5]-t[3:5];
       //m1=int(s[3]-t[3]);
       //m2=int(s[4]-t[4]);

     cout<<to_string(h)":"+to_string(m);
    }
    else
    {

       h= s[0:2]-t[0:2];
       //h1=int(s[0]-t[0]);
      // h2=int(s[1]-t[1]);
       m= s[3:5]-t[3:5];
       //m1=int(s[3]-t[3]);
       //m2=int(s[4]-t[4]);

     cout<<to_string(h)":"+to_string(m);
    }

    return 0;
}
