#include <stdio.h>

void text1() {
    int a,b,c;
    printf("Please enter a,b: ");
    scanf("%d,%d",&a,&b);
    c=a+b;
    printf("%d+%d=%d\n",a,b,c);
}

void text2() {
    float a,b,c,average;
    printf("Please enter a b c: ");
    scanf("%f%f%f",&a,&b,&c);
    average=(a+b+c)/3;
    printf("average=%f\n",average);
}

void text3() {
    int a=10,x=5,y=6;
    a+=a*=6;
    x=y++;
    y=++x;
    a=x+++y;
    printf("%d,%d,%d\n",a,x,y);
}

void text4() {
    int a=5,b=7;
    float x=67.8564,y=-789.124;
    char c='A';
    printf("%3d%3d\n",a,b);
    printf("%10f,%-10f\n",x,y);
    printf("%8.2f,%4f,%c,%10.2c\n",x,y,x,y);
    printf("%c,%d,%o,%x\n",c,c,c,c);
}


#define pi 3.1415926
void text5_1() {
    long d;
    double x;
    scanf("%ld",&d);        //问题一，要加&
    x=1.0/2 * sin(d*pi/180.0);    //问题二，sin函数要小写
    printf("x=%f\n",x);
}

void text5_2() {
    double F,c;
    scanf("%lf",&F);//问题四，要加%lf，输入double类型
    c=5.0/9.0*(F-32.0);
    printf("F=%2.2lf\nc=%2.2lf\n",F,c);//问题三，要加%2.2lf，保留两位小数
}

//#define PRICE 30
void text5_3() {
    int x=5;
    int PRICE=30;
    PRICE=PRICE*x;
    printf("%d%d\n",x,PRICE);
}

void text6() {
    int a,b,t;
    scanf("%d%d",&a,&b);
    printf("a=%db=%d\n",a,b);
    t=a;a=b;b=t;
    printf("a=%db=%d\n",a,b);
}

#include <math.h>
void text7_1() {
    float a,x,y;
    printf("Please enter a x: ");
    scanf("%f%f",&a,&x);
    y=sin(sqrt(a*x))+log(a+x);
    printf("y=%f\n",y);
}

void text7_2() {
    double a,x,y;
    printf("Please enter a x: ");
    scanf("%f%f",&a,&x);
    y=cos(sqrt(a+x)+exp(a*x));
    printf("y=%f\n",y);
}

double area(double a, double b, double c) {
    double s = (a + b + c) / 2;
    return sqrt(s * (s - a) * (s - b) * (s - c));
}

void text7_3() {
    double a = 3.5, b = 5.4, c = 4.3;
    double s = area(a, b, c);  // 调用外部定义的area函数
    printf("area=%f\n", s);
}

int main(void) {
    text1();
    text2();
    text3();
    text4();
    text5_1();
    text5_2();
    text5_3();
    text6();
    text7_1();
    text7_2();
    text7_3();
    return 0;
}