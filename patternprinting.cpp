#include <iostream>
using namespace std;
int main()
{
    int n;
    cout << "plese enter a number";
    cin >> n;
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j < 2 * n + 1; j++)
        {

            if (j == n - i || j == n + i)
            {
                cout << i;
            }

            else
            {
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}