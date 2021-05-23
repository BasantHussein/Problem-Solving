#include <iostream>

using namespace std;

int main()
{
   int n,h,c=0,i,a;
   cin>>n>>h;
   for(i=1;i<=n;i++)
   {
       cin>>a;
       if(a>h)
       {
           c+=2;
       }
       else
       {
           c+=1;
       }
   }
   cout<<c;

    return 0;
}
