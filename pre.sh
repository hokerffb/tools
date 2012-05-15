rsync -razu --progress ~/work/deduct/ sae@10.210.228.15:~/deduct
#scp -r ~/work/deduct/bin sae@10.210.228.15:~/deduct/
#scp -r ~/work/deduct/deduct sae@10.210.228.15:~/deduct/
#scp -r ~/work/deduct/*.sh sae@10.210.228.15:~/deduct/
#scp -r ~/work/deduct/tests sae@10.210.228.15:~/deduct/

rsync -razu --progress --exclude='*.conf' --exclude='.git' ~/work/kanyun/ sae@10.210.228.15:~/kanyun
#scp -r ~/work/kanyun/bin sae@10.210.228.15:~/kanyun/
#scp -r ~/work/kanyun/kanyun sae@10.210.228.15:~/kanyun/
#scp -r ~/work/kanyun/*.sh sae@10.210.228.15:~/kanyun/
#scp -r ~/work/kanyun/tests sae@10.210.228.15:~/kanyun/


rsync -razu --progress ~/gnu/keystone sae@10.210.228.15:~/pyw/
rsync -razu --progress ~/gnu/keystone_client sae@10.210.228.15:~/pyw/
