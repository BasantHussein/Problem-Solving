#include <iostream>

using namespace std;

int main()
{
    int w;
    int n1;
    int n2;
    cin>>w;
    n1=w-2;
    n2=2;
    if((n1%2==0) && (w!=2))
    {
        cout<<"YES";
    }
    else
    {
        cout<<"NO";
    }
    return 0;
}
