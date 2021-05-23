#include <iostream>

using namespace std;

int main()
{
    long long x,c=0,i=0,j;
    cin>>x;
    j=x;
    if(x==1 || x==2 || x==3 || x==4 || x==5)
    {
        c=1;


    }
    else
    {
        while(x!=0)
        {
            j=j-5;
            if(j>=0)
            {
                while(x-5>=0)
                {
                    x=x-5;
                    c++;
                }
                j=x;

            }
            else if(j<0)
            {
                j=x;
            }

            j=j-4;
            if(j>=0)
            {
                while(x-4>=0)
                {
                    x=x-4;
                    c++;

                }
                j=x;

            }
            else if(j<0)
            {
                j=x;
            }

            j=j-3;
            if(j>=0)
            {
                while(x-3>=0)
                {
                     x=x-3;
                     c++;

                }
                j=x;

            }
            else if(j<0)
            {
                j=x;
            }

            j=j-2;
            if(j>=0)
            {
                while(x-2>=0)
                {
                    x=x-2;
                    c++;

                }
                j=x;

            }
            else if(j<0)
            {
                j=x;
            }

            j=j-1;
            if(j>=0)
            {
                while(x-1>=0)
                {
                     x=x-1;
                     c++;

                }
                j=x;

            }
            else if(j<0)
            {
                j=x;
            }


        }

    }
    cout<<c;
    return 0;
}
