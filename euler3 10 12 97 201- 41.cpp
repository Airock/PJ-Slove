#include <iostream>
#include <math.h>
using namespace std;
void problem3()
{
    //The prime factors of 13195 are 5, 7, 13 and 29.
    //What is the largest prime factor of the number 600851475143 ?
    long long max_now =2 ;
    long long ori = 600851475143LL;
    //long long ori = 64;
    for (long long i = 2;i<=ori;)
   {
        if (ori%i != 0)
        {
            i++;
        }
        else
        {
            ori/=i;
            max_now=i;
        }
    }
    cout<<max_now<<endl;
}
//Problem 10
bool isPrim(int i)
{
    for (int j = 2; j*j<=i; j++)
    {
        if (i%j == 0)
        {
            return false;
        }
    }
    return true;
}
void problem10()
{
    //The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    //
    //Find the sum of all the primes below two million
    long long rst=0LL;
    for(int i =2;i<2000000;i++)
    {
        rst+=(isPrim(i)?i:0);
    }
    cout<<rst<<endl;
}
//Problem 12
int numDiv(int input)
{
    int num=0;
    for(int i=1;i*i<input;i++)
        if (input%i==0)
            num+=2;
    
    return num;
    
}
void problem12()
{
    //What is the value of the first triangle number to have over five hundred divisors?
    int i=1;
    int j=1;
    while(numDiv(j)<500)
    {
        i++;
        j=(1+i)*i/2;
    }
    cout<<j<<endl;
}

//problem 97
void problem97()
{
    //28433*2^7830457+1 last ten numbers
    int n = 7830457;
    unsigned int i = 0;
    long long base=2LL;
    for(;i<32;i++)
        if((n<<=1) & 0x80000000)
            break;
    
    for(;i<30;i++)
    {
        long long low = base % 1000000000 ;
        long long high = base / 1000000000;
        base = (low * low) % 10000000000LL + ((2 * high * low) % 10) * 1000000000; 
        n <<= 1;
        if(n&0x80000000)
        {
            base*=2LL;
            base%=10000000000LL;
        }
    }
    cout<<base<<endl;
    cout<<(base*28433LL+1LL)%10000000000LL<<endl;
}
//problem 201 ********************not sloved
#include <bitset>
using std::bitset;
void problem201()
{
    //C(100)(50)= 9332621544394415268169923885626
    //6700490715968264381621468592963895217599993
    //2299156089414639761565182862536979208272237
    //582511852109168640000000000000000000000L
    //caculate this huge number will cost 79981088712 years
    //so need another way.
    const int MAX_NUM=285426;
    unsigned int base[100];
    unsigned int current[50];
    bitset<MAX_NUM> bitmap;
    for(int i = 0;i<100;i++)
        base[i]=(i+1)*(i+1);
    for(int i = 0;i<50;i++)
        current[i]=i;
    
    while(1)
    {
        //update bitmap
        unsigned int sum=0;
        for(int i=0;i<50;i++)
        {
            sum+=base[current[i]];
        }
        bitmap.set(sum);
        
        //update next position
        if(current[49]==99)
        {
            bool changed=false;
            for(int i = 48; i>=0;i--)
                if(current[i]<50+i)
                {
                    changed=true;
                    current[i]++;
                    for(int j = i+1;j<50;j++)
                        current[j]=current[i]+50-i-1;
                    break;
                }
            if (changed == false)
                break;
        }
        else
            current[49]++;
    }
    
    long long rst = 0LL;
    for (int i =0;i<MAX_NUM;i++)
    {
        if(bitmap[i])
            rst+=i;
    }
    cout<<rst<<endl;
}
//problem 41
static int biggest = 0;
void swap(unsigned int* array, unsigned int first, unsigned int second)
{
    unsigned int mid = array[first];
    array[first]=array[second];
    array[second]=mid;
}
void handle(unsigned int* array,unsigned int length)
{
    unsigned int data=0;
     for(int i = 0; i<length;i++)
     {
        data*=10;
        data+=array[i];
     }
     if(isPrim(data))
         biggest=biggest>data?biggest:data;
}
void recursive(unsigned int* array, int length, int pos)
{
    if(pos == length-1)
        handle(array,length);
    else
        for(int i = pos;i<length;i++)
        {
            swap(array,pos,i);
            recursive(array,length,pos+1);
            swap(array,pos,i);
        }
        
}
void problem41()
{
    unsigned int array[9]={1,2,3,4,5,6,7,8,9};
    for(int i = 1;i<10;i++)
        recursive(array,i,0);
    cout<<biggest<<endl;
}
int main ()
{
    problem3();
}








