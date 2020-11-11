#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <signal.h>

int running = 1;

void OnCtrlC(int signo) 
{
    running = 0;
}

int main(int argc, char *argv[])
{
    const int TOTAL = 25 * 60;

    time_t begin = time((time_t*)NULL);
    time_t now = 0;
    printf("\033[?25l"); // hide cursor

    signal(SIGINT, OnCtrlC);

    while (running) {
        now = time((time_t*)NULL);
        time_t pass = now - begin;
        if (pass > TOTAL) {
            break;
        }
        time_t count = TOTAL - pass;

        int min = count / 60;
        int second = count % 60;
        printf("\r\033[k%02d:%02d", min, second);

        usleep(100);
    }

    printf("\033[?25h"); // show cursor
    printf("\n");

    return 0;
}