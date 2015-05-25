sysbench  --test=cpu --cpu-max-prime=20000 run
sysbench --test=memory --memory-block-size=8K --memory-total-size=2G  --num-threads=16 run
sysbench --test=fileio --file-total-size=1G prepare
sysbench --test=fileio --file-total-size=1G --file-test-mode=rndwr run
sysbench --test=fileio --file-total-size=1G --file-test-mode=rndwr cleanup
