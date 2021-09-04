#include <stdio.h>
#include "unistd.h"
#include <sys/wait.h>
#include <stdlib.h>

void show_usage() {
    printf("Usage:\n");
    printf("pwatchdog \"command\"\n");
}

int execwait(char *cmd) {
    system(cmd);
    return 0;
}

int main(int argc, char *argv[]) {
    int count = 0;
    if (argc < 2) {
        show_usage();
        return 0;
    }
    do {
        count++;
        execwait(argv[1]);
        printf("Restart %d times...\n", count);
        sleep(1);
    } while (1);
   
    return 0;
}