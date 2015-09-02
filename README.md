tools
=====

Best tools for working


# Tools

## fdp

Format 'docker ps' output

## where

Look if the python moudle exist

usage:
$ where <python-moudle-name> 

## ref

Highlight the word in grep's output

# Install

```
sudo ./install.sh
```

# Example

```
$ grep -rnE "\.get_all\(" *|ref 5 5 "get_all"
$ docker ps|fdp
```
