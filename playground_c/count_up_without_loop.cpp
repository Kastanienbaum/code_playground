/*
* src: https://qr.ae/TWtPnB 
*/

#include <iostream>
 
using namespace std;
 
class Demo
{
    private:
        int num = 0;
    public:
        static int count;
    
    Demo()
    {
        count++;
        num = count;
        cout << num << endl;
    }
};
 
// count is of type static and initialized outside of a scope 
int Demo::count = 0;
 
int main()
{
    Demo A[100];
    cin.get();
    return 0;
}