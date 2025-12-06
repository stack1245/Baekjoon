#include <stdio.h>

int main()
{
    int n;
    int arr[101];
    int v;
    int count = 0;

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    scanf("%d", &v);

    for (int i = 0; i < n; i++)
    {
        if (arr[i] == v)
        {
            count++;
        }
    }

    printf("%d\n", count);

    return 0;
}
