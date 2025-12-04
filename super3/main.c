#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

int main() {
    int random_num, guess_num;
    int count = 0;  // 猜的次数计数器
    int min_range = 1, max_range = 100;  // 初始范围

    // 设置随机数种子
    srand(time(NULL));
    // 生成1~100的随机数
    random_num = rand() % 100 + 1;

    printf("=== 猜数字游戏 ===\n");
    printf("我已经想好了一个1~100之间的数字，请你来猜！\n\n");

    do {
        printf("请输入%d~%d之间的数字: ", min_range, max_range);
        scanf("%d", &guess_num);
        count++;  // 猜的次数加1

        // 检查输入是否在有效范围内
        if (guess_num < min_range || guess_num > max_range) {
            printf("输入错误！请输入%d~%d之间的数字。\n", min_range, max_range);
            continue;
        }

        if (guess_num > random_num) {
            printf("比%d小！", guess_num);
            // 更新范围上限
            max_range = guess_num - 1;
            printf("请重新输入%d~%d之间的数字。\n", min_range, max_range);
        }
        else if (guess_num < random_num) {
            printf("比%d大！", guess_num);
            // 更新范围下限
            min_range = guess_num + 1;
            printf("请重新输入%d~%d之间的数字。\n", min_range, max_range);
        }
        else {
            // 猜对了
            printf("\n恭喜你！猜对了！\n");
            printf("正确答案就是：%d\n", random_num);
            printf("你一共猜了%d次。\n", count);

            // 根据猜测次数给出评价
            if (count <= 3) {
                printf("太厉害了！你是天才！\n");
            }
            else if (count <= 7) {
                printf("不错哦，运气很好！\n");
            }
            else if (count <= 15) {
                printf("表现还可以，继续加油！\n");
            }
            else {
                printf("有点慢哦，要多练习！\n");
            }
        }

        printf("\n");

    } while (guess_num != random_num);
    system("pause");
    return 0;
}