#include <iostream>

using namespace std;

int main()
{
   static unsigned x,countt=1,sum=1,c2=1;
    cin>>x;
    while(countt<x)
    {
        countt=countt*2;
    }
    if(countt==x)
    {
        sum=1;
    }
    else if(countt>x)
    {
        countt=countt/2;
        if(countt+sum==x)
        {
            sum+=1;
        }
        else
        {
            while(countt!=x)
            {
                if(countt+1==x)
                {
                    sum+=1;
                    countt=countt+1;
                }
                if(countt+sum==x)
                {
                    sum+=1;
                    countt=countt+sum;
                    break;
                }

                if(countt==x)
                {
                    break;
                }
                else
                {
                 sum+=1;
                 c2=c2*2;
                 countt=countt+c2;


                }
            }
        }


    }

    cout<<sum;
    return 0;
}
