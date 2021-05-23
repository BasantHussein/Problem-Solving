#include <iostream>

using namespace std;

int main()
{
    int t,px,py,x=0,y=0,i,j,cu=0,cd=0,cr=0,cl=0,flagn=0;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        x=0,y=0,cu=0,cd=0,cr=0,cl=0,flagn=0;
        cin>>px>>py;
        string s;
        cin>>s;
        for(j=0;j<s.size();j++)
        {
            if(s[j]=='U')
            {
                y++;
                cu++;
            }
            else if(s[j]=='D')
            {
                y--;
                cd++;
            }
            else if(s[j]=='R')
            {
                x++;
                cr++;
            }
            else if(s[j]=='L')
            {
                x--;
                cl++;
            }

        }

        while((x!=px || y!=py) && flagn!=1)
        {
            if(y>py && cu>0)
            {
                cu--;
                y--;

            }
           else if(y<py && cd>0)
            {
                cd--;
                y++;

            }
           else if(x>px && cr>0)
            {
                cr--;
                x--;

            }
           else if(x<px && cl>0)
            {
                cl--;
                x++;

            }
            else
            {
                flagn=1;
            }
        }
            if(flagn==1 && (x!=px || y!=py))
            {
                cout<<"No"<<"\n";
            }
            else if(x==px && y==py)
            {
                cout<<"Yes"<<"\n";
            }
            else
            {
                cout<<"Yes"<<"\n";
            }



    }

    return 0;
}
