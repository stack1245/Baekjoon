#include <stdio.h>

int main()
{
    int H, M, cookTime;

    scanf("%d %d", &H, &M);
    scanf("%d", &cookTime);

    M += cookTime;

    H += M / 60;
    M = M % 60;

    H = H % 24;

    printf("%d %d\n", H, M);

    return 0;
}
