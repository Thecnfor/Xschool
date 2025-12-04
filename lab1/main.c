#include <stdio.h>

void que2() {
    for (int i =1;i<=7;i+=2) {
        for (int j=0; j<i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

void que3() {
    char c1,c2;
    c1=97,c2=98;
    printf("%c %c\n",c1,c2);
}

void que4() {
    int a,b,c,d;
    unsigned u,v;
    a=1,b=3,c=6,d=-7;
    u=a+b;
    v=c+d;
    printf("u=%d,v=%d\n",u,v);
}

int main(void) {
    que2();
    que3();
    que4();
    return 0;
}