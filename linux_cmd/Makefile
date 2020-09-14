.DEFAULT_GOAL := all

CC=gcc
CFLAGS=-Wall -g

base : cax.c ai.c
	$(CC) $(CFLAGS) cax.c -o cax.out
	$(CC) $(CFLAGS) ai.c -o ai.out

install: cax.out
	@cp -f cax.out /usr/local/bin/cax
	@cp -f ai.out /usr/local/bin/ai

uninstall:
	@rm -f /usr/local/bin/cax
	@rm -f /usr/local/bin/ai
	
.PHONY : all
all : base

clean:
	@rm -f *.o
	@rm -f *.out
	@rm -rf *.out.*