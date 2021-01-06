.DEFAULT_GOAL := all

CC=gcc
CFLAGS=-Wall -g -O0

base : cax.c ai.c
	$(CC) $(CFLAGS) cax.c -o cax.out
	$(CC) $(CFLAGS) ai.c -o ai.out
	$(CC) $(CFLAGS) pt.c -o pt.out

install: cax.out pt.out ai.out
	@cp -f pt.out /usr/local/bin/pt
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
	@rm -f /usr/local/bin/pt
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