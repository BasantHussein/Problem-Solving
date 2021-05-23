#include <iostream>

using namespace std;

int main()
{
    int n,c=0,i,x;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>x;
        if(x==1)
        {
            c=1;
        }

    }
    if (c==1)
    {
        cout<<"HARD";
    }
    else
    {
        cout<<"EASY";
    }


    return 0;
}
