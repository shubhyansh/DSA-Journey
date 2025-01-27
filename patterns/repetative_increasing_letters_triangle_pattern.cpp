#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    char ch='A';
    for(int i=0;i<n;i++){
         char pr = ch+i;
        for (int j=0;j<=i;j++){
           
            cout<<pr;
        }
        
        cout<<'\n';
    }
    

    return 0;
}