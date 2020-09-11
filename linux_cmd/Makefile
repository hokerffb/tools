.DEFAULT_GOAL := all

CC=gcc
CFLAGS=-Wall -g

base : cax.c
	$(CC) $(CFLAGS) cax.c -o cax.out

install: cax.out
	@cp -f cax.out /usr/local/bin/cax

uninstall:
	@rm -f /usr/local/bin/cax
	
.PHONY : all
all : base

clean:
	@rm -f *.o
	@rm -f *.out
	@rm -rf *.out.*