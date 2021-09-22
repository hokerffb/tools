.PHONY : all
all : base

.DEFAULT_GOAL := all
CC=gcc
CFLAGS=-Wall -g -O0 -DDEBUG
RELEASEFLAGS=-Wall

base : cax.c ai.c
	$(CC) $(CFLAGS) cax.c -o cax.out
	$(CC) $(CFLAGS) ai.c -o ai.out
	$(CC) $(CFLAGS) fq.c -o fq.out

release: cax.c ai.c fq.c
	$(CC) $(RELEASEFLAGS) cax.c -o cax.out
	$(CC) $(RELEASEFLAGS) ai.c -o ai.out
	$(CC) $(RELEASEFLAGS) fq.c -o fq.out

install: cax.out fq.out ai.out
	@cp -f fq.out /usr/local/bin/fq
	@cp -f cax.out /usr/local/bin/cax
	@cp -f ai.out /usr/local/bin/ai
	@cp -f ./where.py /usr/local/bin/wherepy
	@chmod +x /usr/local/bin/wherepy
	@cp -f ./ref.py /usr/local/bin/ref
	@chmod +x /usr/local/bin/ref
	@cp -f ./fdp.py /usr/local/bin/fdp
	@chmod +x /usr/local/bin/fdp
	@cp -f ./downts.py /usr/local/bin/downts
	@chmod +x /usr/local/bin/downts

uninstall:
	@rm -f /usr/local/bin/fq
	@rm -f /usr/local/bin/cax
	@rm -f /usr/local/bin/ai
	@rm -f /usr/local/bin/wherepy
	@rm -f /usr/local/bin/ref
	@rm -f /usr/local/bin/fdp
	@rm -f /usr/local/bin/downts

clean:
	@rm -f *.o
	@rm -f *.out
	@rm -rf *.out.*