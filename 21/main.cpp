#include <iostream>
#include <bitset>

using namespace std;
unsigned int sumd(int input)
{
    unsigned int output=0;
    for(int i = 2;i*i<input;i++)
    {
        if(input%i==0)
        {
            output+=i;
            output+=input/i;
        }
    }
    return output+1;
}
int main()
{
    bitset<10000> bitmap;
    unsigned int total=0;
    for(int i =1;i<10000;)
    {
        unsigned int sumd_i=sumd(i);
        bitmap[i]=1;
        if(sumd_i<10000)
            bitmap[sumd_i]=1;
        if(sumd_i<10000 && sumd_i!=i && sumd(sumd_i)==i)
        {
            total+=i;
            cout<<i<<endl;
            cout<<sumd_i<<endl;
            total+=sumd_i;
        }

        while(bitmap[i]==1 && i<10000)
            i++;

    }
    cout<<total<<endl;
    //cout << "Hello world!" << endl;
    return 0;
}
