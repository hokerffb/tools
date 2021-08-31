.DEFAULT_GOAL := all
.PHONY : all
all : readme

readme:
	@echo 'Remove water-mark from x-mind export png file.'
	@echo 'Usage:'
	@echo '  rx src dest'

install: rx.py
	@cp -f rx.py /usr/local/bin/rx
	@chmod +x /usr/local/bin/rx

uninstall:
	@rm -f /usr/local/bin/rx

clean:
	@rm -f *.pyc