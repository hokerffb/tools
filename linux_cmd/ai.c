#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/shm.h>

/********************************************** 
Auto Increase cmd
Usage:
ai [start]|[end]
ai start [init number] [step]
ai [this]
$ ai start 0 1
$ wget http://movie.net/1.mp4  land_`ai`.mp4
$ wget http://movie.net/2.mp4  land_`ai`.mp4
$ echo "`ai this`"
$ ai end
$ ls
land_1.mp4 land_2.mp4

实现：
进程间通讯
ai start启动进程，计数器=init number
ai 计数器+step，输出
ai end 进程结束
**********************************************/

typedef struct _Counter {
    int counter;
    int step;
} Counter;


void show_usage(void)
{
    printf("ai: Auto Increase number v1.0\n");
    printf("Usage:\n");
    printf("\tai [start] | [end]\n");
    printf("\tai start [init number] [step]\n");
    printf("\tai [this]|[noecho]");
    printf("\tai\n");
    printf("\tai end\n\n");
    printf("Sample:\n");
    printf("$ ai start 0 1\n");
    printf("$ wget http://movie.net/1.mp4  land_`ai`.mp4\n");
    printf("$ wget http://movie.net/2.mp4  land_`ai`.mp4\n");
    printf("$ echo \"`ai this`\"\n");
    printf("$ ai noecho\n");
    printf("$ ai end\n");
    printf("$ ls\n");
    printf("land_1.mp4 land_2.mp4\n");
}

int main(int argc, char * argv[])
{
    int shmid = 0;
    void *shm = NULL;
    Counter counter = {0};

    if (argc == 2 && strcmp(argv[1], "--help") == 0)
    {
        show_usage();
        return 0;
    }
    
    shmid = shmget((key_t)0xFF, sizeof(Counter), 0666|IPC_CREAT);
    shm = shmat(shmid, (void*)0, 0);
    
    counter = *((Counter *)shm);
    if (argc >= 3) {
        // ai start [init number] [step]
        counter.counter = atoi(argv[2]);
        counter.step = 1;
        if (argc == 4) {
            counter.step = atoi(argv[3]);
        }
        memcpy(shm, &counter, sizeof(Counter));
    } else if (argc == 1) {
        // ai
        counter.counter += counter.step;
        memcpy(shm, &counter, sizeof(Counter));
        printf("%d", counter.counter);
    } else if (argc == 2) {
        if (strcmp(argv[1], "start") == 0) {
            counter.counter = 0;
            counter.step = 1;
            memcpy(shm, &counter, sizeof(Counter));
        } else if (strcmp(argv[1], "end") == 0) {
            // ai end
            shmdt(shm);
            shmctl(shmid, IPC_RMID, 0);
        } else if (strcmp(argv[1], "this") == 0) {
            printf("%d", counter.counter);
        } else if (strcmp(argv[1], "noecho") == 0) {
            counter.counter += counter.step;
            memcpy(shm, &counter, sizeof(Counter));
        }
    }
    
    return 0;
}