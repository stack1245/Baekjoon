#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    double score[1000];
    double max = 0;

    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &score[i]);
        if (score[i] > max)
            max = score[i];
    }

    double sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += score[i] / max * 100;
    }

    printf("%.2lf\n", sum / n);

    return 0;
}
