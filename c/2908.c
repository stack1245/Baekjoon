#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);

    int ra = (a % 10) * 100 + (a / 10 % 10) * 10 + a / 100;
    int rb = (b % 10) * 100 + (b / 10 % 10) * 10 + b / 100;

    printf("%d\n", ra > rb ? ra : rb);
    return 0;
}
