#include <iostream>

using namespace std;

int main()
{
    long long k,n,w,i,sum=0,c=0;
    cin>>k>>n>>w;
    for(i=1;i<=w;i++)
    {
        sum+=i*k;

    }
    if(sum>n)
    {
        c=sum-n;
    }
    cout<<c;

    return 0;
}
