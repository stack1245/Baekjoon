#include <stdio.h>
#include <string.h>

int main()
{
    char s[101];
    int pos[26];
    scanf("%s", s);

    for (int i = 0; i < 26; i++)
        pos[i] = -1;

    for (int i = 0; i < strlen(s); i++)
    {
        int idx = s[i] - 'a';
        if (pos[idx] == -1)
            pos[idx] = i;
    }

    for (int i = 0; i < 26; i++)
        printf("%d ", pos[i]);

    return 0;
}
