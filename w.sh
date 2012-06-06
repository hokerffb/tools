
for i in `seq 1 $1`;
do
    gnome-terminal -t 15 -x ssh ubuntu@10.210.228.1
done
ssh ubuntu@10.210.228.1
