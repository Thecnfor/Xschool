#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n, player, computer;
    srand(time(0));  // 初始化随机数种子

    printf("请输入比赛次数：");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("\n第 %d 局\n", i + 1);
        printf("请输入 (0=石头, 1=剪刀, 2=布): ");
        scanf("%d", &player);

        // 输入验证
        if (player < 0 || player > 2) {
            printf("输入无效，请输入 0~2。\n");
            i--; // 保持局数不变
            continue;
        }

        computer = rand() % 3;  // 随机生成0~2

        // 输出玩家选择（使用switch）
        switch (player) {
            case 0:
                printf("你出的是：石头\n");
                break;
            case 1:
                printf("你出的是：剪刀\n");
                break;
            case 2:
                printf("你出的是：布\n");
                break;
        }

        // 输出电脑选择（使用switch）
        switch (computer) {
            case 0:
                printf("电脑出的是：石头\n");
                break;
            case 1:
                printf("电脑出的是：剪刀\n");
                break;
            case 2:
                printf("电脑出的是：布\n");
                break;
        }

        // 判断输赢（使用switch，不使用逻辑符号）
        switch (player) {
            case 0: // 玩家出石头
                switch (computer) {
                    case 0:
                        printf("结果：平局！\n");
                        break;
                    case 1:
                        printf("结果：你赢了！\n");
                        break;
                    case 2:
                        printf("结果：电脑赢了！\n");
                        break;
                }
                break;
            case 1: // 玩家出剪刀
                switch (computer) {
                    case 0:
                        printf("结果：电脑赢了！\n");
                        break;
                    case 1:
                        printf("结果：平局！\n");
                        break;
                    case 2:
                        printf("结果：你赢了！\n");
                        break;
                }
                break;
            case 2: // 玩家出布
                switch (computer) {
                    case 0:
                        printf("结果：你赢了！\n");
                        break;
                    case 1:
                        printf("结果：电脑赢了！\n");
                        break;
                    case 2:
                        printf("结果：平局！\n");
                        break;
                }
                break;
        }
    }

    printf("\n比赛结束！感谢参与～\n");
    return 0;
}