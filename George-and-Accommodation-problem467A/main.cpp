#include <iostream>

using namespace std;

int main()
{
    int t,i,p,q,c=0,sum=0;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>p>>q;
        sum=q-p;
        if(sum>=2)
        {
            c++;
        }

    }
    cout<<c;
    return 0;
}
