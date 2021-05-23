#include <iostream>

using namespace std;

int main()
{
long long s,v1,v2,t1,t2,first,second;
cin>>s>>v1>>v2>>t1>>t2;

first = (v1*s) + (t1 * 2);
second = (v2*s) + (t2 * 2);
//if ((v1 >= s || v1 < t1) and (v2 >= s || v2 < t2))
//{
     //cout<<"Friendship";
//}

 if(first < second)
{
    cout<<"First";
}
else if(second < first)
{
    cout<<"Second";
}
else
{
    cout<<"Friendship";
}

    return 0;
}
