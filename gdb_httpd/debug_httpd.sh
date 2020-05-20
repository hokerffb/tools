pids=$(ps -ef|grep httpd\:|grep nobody|awk '{print $2}'|head -n $1|tail -n 1)
for pid in $pids
do
    echo "--------------------------------------"
    echo "pid="$pid
    gdb /usr/local/sae/httpd/bin/httpd --pid=$pid <<!
c
bt
!
echo
done

