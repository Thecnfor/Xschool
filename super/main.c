/*
 * @ASCII对照
 * 65(A)-90(Z) 大写字母
 * 97(a)-122(z) 小写字母
 * @加密规则:ASCII码加4取模26
 */
#include <stdio.h>

int main() {
    char c;

    printf("输入字符串:");

    // 逐个读取字符直到换行符
    while ((c = getchar()) != '\n') {
        // 小写字母加密
        if (c >= 'a' && c <= 'z') {
            c = ((c - 'a' + 4) % 26) + 'a';
        }
        // 大写字母加密
        else if (c >= 'A' && c <= 'Z') {
            c = ((c - 'A' + 4) % 26) + 'A';
        }

        printf("%c", c);  // 立即输出加密后的字符
    }

    printf("\n");
    return 0;
}