tools
=====

Best tools for working


[where]

install:
sudo cp ./where.py /usr/bin/where
sudo chmod +x /usr/bin/where

use:
$ where <python-moudle-name> 

[ref]

install:
sudo cp ./ref.py /usr/bin/ref
sudo chmod +x /usr/bin/ref

use:
$ grep -rnE "\.get_all\(" *|ref 5 5 "get_all"
