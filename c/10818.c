#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int min = 1000000;
    int max = -1000000;
    
    for (int i = 0; i < n; i++) {
        int num;
        scanf("%d", &num);
        
        if (num < min) {
            min = num;
        }
        if (num > max) {
            max = num;
        }
    }
    
    printf("%d %d\n", min, max);
    
    return 0;
}
