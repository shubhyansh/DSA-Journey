#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    
    for(int i=0;i<n;i++){
        
         
        for (int j=n-i;j>0;j--){
           cout<<"*";
            
        }
        for(int j=0;j<i*2;j++){
            cout<<" ";
        }
        for (int j=n-i;j>0;j--){
           cout<<"*";
            
        }
        
        cout<<'\n';
    }
    for(int i=0;i<n;i++){
        
         
        for (int j=0;j<=i;j++){
           cout<<"*";
            
        }
        for(int j=0;j<2*n-2-2*i;j++){
            cout<<" ";
            
        }
        for (int j=0;j<=i;j++){
           cout<<"*";
            
        }
        
        
        cout<<'\n';
    }
    

    return 0;
}