#include <stdio.h>

int main()
{
    int n, m, i, j, k;
    int basket[101] = {0};

    scanf("%d %d", &n, &m);

    for (int a = 0; a < m; a++)
    {
        scanf("%d %d %d", &i, &j, &k);
        for (int b = i; b <= j; b++)
        {
            basket[b] = k;
        }
    }

    for (int a = 1; a <= n; a++)
    {
        printf("%d ", basket[a]);
    }

    return 0;
}
