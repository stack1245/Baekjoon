#include <stdio.h>

int main() {
    int max = 0;
    int position = 0;
    
    for (int i = 1; i <= 9; i++) {
        int n;
        scanf("%d", &n);
        
        if (n > max) {
            max = n;
            position = i;
        }
    }
    
    printf("%d\n%d\n", max, position);
    
    return 0;
}
