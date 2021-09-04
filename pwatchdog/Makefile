.DEFAULT_GOAL := all

CC=clang
CFLAGS=-Wall -g -O0

.PHONY : all
all : main

main : pwatchdog.c
	$(CC) $(CFLAGS) pwatchdog.c -o pwatchdog.out

install: pwatchdog.out
	@cp -f pwatchdog.out /usr/local/bin/pwatchdog
	@chmod +x /usr/local/bin/pwatchdog

uninstall:
	@rm -f /usr/local/bin/pwatchdog

clean:
	@rm -f *.o
	@rm -f *.out
	@rm -rf *.out.*