#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int i=1;i<=2*n-1;i++){
        for(int j=1;j<=2*n-1;j++){
            int left=j-1;
            int right=2*n-1-j;
            int top=i-1;
            int bottom=2*n-1-i;
            int current=n-min(min(left,right),min(top,bottom));
            cout<<current;
        }
        cout<<"\n";
    }
    
    
    
    return 0;
}