#include <stdio.h>
#include <string.h>

int main()
{
    int t;
    char s[1001];
    scanf("%d", &t);
    while (t--)
    {
        scanf("%s", s);
        int len = strlen(s);
        printf("%c%c\n", s[0], s[len - 1]);
    }
    return 0;
}
