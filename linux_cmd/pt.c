#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>
#include <string.h>

int running = 1;

void OnCtrlC(int signo) 
{
    // user quit
    running = 0;
}

int main(int argc, char *argv[])
{
    int TOTAL = 25 * 60;
    printf("%d -> %s\n", argc, argv[1]);
    if (argc > 2 && strcmp(argv[1], "-t")==0) {
        // pt -t 1
        printf("\t%d -> %s\n", argc, argv[2]);
        TOTAL = atoi(argv[2]) * 60;
    }

    time_t begin = time((time_t*)NULL);
    time_t now = 0;
    printf("\033[?25l"); // hide cursor

    signal(SIGINT, OnCtrlC);

    while (running) {
        now = time((time_t*)NULL);
        time_t pass = now - begin;
        if (pass > TOTAL) {
            // normal quit
            break;
        }
        time_t count = TOTAL - pass;

        int min = count / 60;
        int second = count % 60;
        printf("\r\033[k%02d:%02d", min, second);

        usleep(100);
    }

    printf("\033[?25h"); // show cursor
    printf("\a");
    printf("\n");
    // MacOS: afplay end.mp3
    if (running) {
        system("afplay ~/Music/end.mp3 &");
    }

    return 0;
}