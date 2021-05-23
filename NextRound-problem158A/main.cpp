#include <iostream>

using namespace std;

int main()
{
    int n,k,i,s,c=0,j,c2=0;
    cin>>n>>k;
    int a[n];
    for(i=0;i<n;i++)
    {
        cin>>a[i];

    }
    s=a[k-1];
    for(j=0;j<n;j++)
    {
        if(a[j]==0)
        {
            c2++;
        }
        if(c2==n)
        {
            c=0;
        }
        else if(a[j]>=s && c2!=n && a[j]!=0)
        {
            c++;
        }
    }
    cout<<c;

    return 0;
}
