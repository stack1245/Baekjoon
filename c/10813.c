#include <stdio.h>

int main()
{
    int n, m, i, j, temp;
    int basket[101];

    scanf("%d %d", &n, &m);

    for (int a = 1; a <= n; a++)
    {
        basket[a] = a;
    }

    for (int a = 0; a < m; a++)
    {
        scanf("%d %d", &i, &j);
        temp = basket[i];
        basket[i] = basket[j];
        basket[j] = temp;
    }

    for (int a = 1; a <= n; a++)
    {
        printf("%d ", basket[a]);
    }

    return 0;
}
