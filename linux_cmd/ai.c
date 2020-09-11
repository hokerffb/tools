#include <stdio.h>

/********************************************** 
Auto Increase cmd
Usage:
ai [start]|[end]
ai start [init number] [step]
$ ai start 0 1
$ wget http://movie.net/1.mp4  land_`ai`.mp4
$ wget http://movie.net/2.mp4  land_`ai`.mp4
$ ai end
$ ls
land_1.mp4 land_2.mp4

实现：
进程间通讯
ai start启动进程，计数器=init number
ai 计数器+step，输出
ai end 进程结束
**********************************************/

int main(int argc, char* args[])
{
    // TODO：就差干活的了
    printf("%d", 0);
    return 0;
}