.DEFAULT_GOAL := all

CC=gcc
CFLAGS=-Wall -g

base : cax.c ai.c
	$(CC) $(CFLAGS) cax.c -o cax.out
	$(CC) $(CFLAGS) ai.c -o ai.out

install: cax.out
	@cp -f cax.out /usr/local/bin/cax
	@cp -f ai.out /usr/local/bin/ai
	@cp -f ./where.py /usr/bin/where
	@chmod +x /usr/bin/where
	@cp -f ./ref.py /usr/bin/ref
	@chmod +x /usr/bin/ref
	@cp -f ./fdp.py /usr/bin/fdp
	@chmod +x /usr/bin/fdp
	@cp -f ./downts.py /usr/bin/downts
	@chmod +x /usr/bin/downts


uninstall:
	@rm -f /usr/local/bin/cax
	@rm -f /usr/local/bin/ai
	@rm -f /usr/local/bin/wherepy
	@rm -f /usr/local/bin/ref
	@rm -f /usr/local/bin/fdp
	@rm -f /usr/local/bin/downts
	
.PHONY : all
all : base

clean:
	@rm -f *.o
	@rm -f *.out
	@rm -rf *.out.*