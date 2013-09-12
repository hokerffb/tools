rm -f logs/*
for i in $(seq 1 1 100)
do
    sh clean_nouse.sh
    python mt.py
done
