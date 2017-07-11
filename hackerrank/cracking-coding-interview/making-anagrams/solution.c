#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    char* a = (char *)malloc(512000 * sizeof(char));
    scanf("%s",a);
    char* b = (char *)malloc(512000 * sizeof(char));
    scanf("%s",b);
    
    int c[26];
    unsigned int i;
    for (i = 0; i < 26; i++) {        
        *(c+i) = 0;
    }
    
    for (i = 0; i < strlen(a); i++) {        
        *(c + *(a+i) - 'a') += 1;
    }
    for (i = 0; i < strlen(b); i++) {        
        *(c + *(b+i) - 'a') -= 1;
    }
    
    int t = 0;
    for (i = 0; i < 26; i++) {
        t += abs(*(c+i));
    }
    printf("%d", t);    
    
    return 0;
}