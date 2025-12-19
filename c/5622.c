#include <stdio.h>
#include <string.h>

int main()
{
    char s[16];
    int time = 0;
    scanf("%s", s);

    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] >= 'A' && s[i] <= 'C')
            time += 3;
        else if (s[i] >= 'D' && s[i] <= 'F')
            time += 4;
        else if (s[i] >= 'G' && s[i] <= 'I')
            time += 5;
        else if (s[i] >= 'J' && s[i] <= 'L')
            time += 6;
        else if (s[i] >= 'M' && s[i] <= 'O')
            time += 7;
        else if (s[i] >= 'P' && s[i] <= 'S')
            time += 8;
        else if (s[i] >= 'T' && s[i] <= 'V')
            time += 9;
        else if (s[i] >= 'W' && s[i] <= 'Z')
            time += 10;
    }

    printf("%d\n", time);
    return 0;
}
