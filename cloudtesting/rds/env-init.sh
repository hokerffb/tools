##########################################
#
# 1. create a database user: testuser
# 2. create database: bench
# 3. execute 'sh run.sh' script
#
###########################################
 
apt-get install -y git vim
apt-get install -y mysql-client-core-5.5 python-mysqldb

# init tables
# must create database first 
SQL="CREATE TABLE  `ins-test`.`ins` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,`value` VARCHAR( 1024 ) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL) ENGINE = MYISAM ;"
mysql -h$MYSQLHOST -P$MYSQLPORT -u$MYSQLUSER -p$MYSQLPASS -e "$SQL" 

