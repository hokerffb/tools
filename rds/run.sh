# MYSQLHOST="rds5p8m18evd4h4kcs1td.mysql.rds.aliyuncs.com"
# MYSQLPORT="3306"
# MYSQLUSER="testuser"
# MYSQLPASS="1a2b3c4d"
# MYSQLDB="bench"

mysql -hMYSQLHOST -PMYSQLPORT -uMYSQLUSER -pMYSQLPASS -e "create database $MYSQLDB;"

sysbench --num-threads=16 --test=oltp --mysql-table-engine=innodb --mysql-host=$MYSQLHOST --mysql-port=$MYSQLPORT --mysql-db=$MYSQLDB --oltp-table-size=2000000 --max-time=1200 --mysql-user=$MYSQLUSER --mysql-password=$MYSQLPASS prepare

sysbench --num-threads=16 --test=oltp --mysql-table-engine=innodb --mysql-host=$MYSQLHOST --mysql-port=$MYSQLPORT --mysql-db=$MYSQLDB --oltp-table-size=2000000 --max-time=1200 --mysql-user=$MYSQLUSER --mysql-password=$MYSQLPASS --max-time=120 run

sysbench --num-threads=16 --test=oltp --mysql-table-engine=innodb --mysql-host=$MYSQLHOST --mysql-port=$MYSQLPORT --mysql-db=$MYSQLDB --oltp-table-size=2000000 --max-time=1200 --mysql-user=$MYSQLUSER --mysql-password=$MYSQLPASS --max-time=120 cleanup

