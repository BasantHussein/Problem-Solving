#include <iostream>

using namespace std;

int main()
{
    int n,m,c=0;
    cin>>n>>m;
    while(n!=0 && m!=0)
    {
        n--;
        m--;
        if(c==0)
        {
            c=1;
        }
        else
        {
            c=0;
        }
    }
    if(c==0)
    {
        cout<<"Malvika"<<"\n";
    }
    else
    {
        cout<<"Akshat"<<"\n";
    }


    return 0;
}
