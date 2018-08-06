
# codeproxy

codeproxy.py run into server
upload,py to upload code


## usage

```
    upload                  - run run.sh in server
    upload -c "command"     - execute command in server and get return value
    upload "shell"          - run shell script in server and get output
```


## example


```
$ ./upload.py "df -h"
$ df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/sdb1              28G   24G  3.3G  88% /
udev                  1.9G  4.0K  1.9G   1% /dev
tmpfs                 791M  436K  791M   1% /run
none                  5.0M     0  5.0M   0% /run/lock
none                  2.0G  4.0M  2.0G   1% /run/shm
/dev/sdb5             105G   12G   89G  12% /var

$ ./upload.py
run pre.sh in client,run run.sh in server
```
