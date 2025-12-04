#include <stdio.h>

void t1_1() {
    if(5)
        printf("%d if true\n",5);
    else
        printf("%d if false\n",5);
}

void t1_2() {
    int a=5;
    if(a==6)
        printf("=\n");
    else
        printf("! =\n");
}

void t_3() {
    int a=5,b=4,c=3,d=2;
    if(a>b>c)
        printf("%d\n", d);
    else if((c-1>=d)==1)
        printf("%d\n",d+1);
    else
        printf("%d\n",d+2);
}

void t_5() {
    char a='z';
    int c=5;
    switch(a++) {
        case 'z':c++;
        case 'x':c+=20;break;
        case 'y':c-=15;break;
    }
    printf("%d\n" ,c);
}

void t_6() {
    int i=1,sum=0;
    while(i<10) {
        sum+=i;
        i=i+2;
    }
    printf("%d\n",sum);
}

void t_7() {
    int i,s;
    for(i=1;i<=3;i++)
        s+=i;
    printf("%d\n",s);
}

void t_10() {
    int i,j,x=0;
    for(i=0;i<2;i++) {
        x++;
        for(j=0;j<3;j++) {
            if(j%2) continue;
            x++;
        }
        x++;
    }
    printf ("x = %d\n",x);
}
int main() {
    t_3();
    t_6();
    t_10();
    return 0;
}