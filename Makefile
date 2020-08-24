.DEFAULT_GOAL := all

install : where.py ref.py fdp.py downts.py
	cp ./where.py /usr/local/bin/wherepy
	chmod +x /usr/local/bin/wherepy

	cp ./ref.py /usr/local/bin/ref
	chmod +x /usr/local/bin/ref

	cp ./fdp.py /usr/local/bin/fdp
	chmod +x /usr/local/bin/fdp

	cp ./downts.py /usr/local/bin/downts
	chmod +x /usr/local/bin/downts


.PHONY : all
all : install

clean:
	@rm -f /usr/local/bin/wherepy
	@rm -f /usr/local/bin/ref
	@rm -f /usr/local/bin/fdp
	@rm -f /usr/local/bin/downts