#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);

    int count = N / 4;
    for (int i = 0; i < count; i++)
    {
        printf("long ");
    }
    printf("int\n");

    return 0;
}
