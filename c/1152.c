#include <stdio.h>
#include <string.h>

int main()
{
    char s[1000001];
    int cnt = 0;
    fgets(s, 1000001, stdin);

    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == ' ' || s[i] == '\n')
        {
            if (i > 0 && s[i - 1] != ' ' && s[i - 1] != '\n')
                cnt++;
        }
    }

    if (strlen(s) > 0 && s[strlen(s) - 1] != ' ' && s[strlen(s) - 1] != '\n')
        cnt++;

    printf("%d\n", cnt);
    return 0;
}
