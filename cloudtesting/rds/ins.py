import time
import MySQLdb

count = 0

class options:
    mysql_host="rds5p8m18evd4h4kcs1td.mysql.rds.aliyuncs.com"
    mysql_db="ins-test"
    mysql_user="testuser"
    mysql_password="1a2b3c4d"

def test_insert():
    global count
    conn = MySQLdb.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_db)
    sql = 'insert into ins(value) values("%s")' % ("." * 1024)
    cur = conn.cursor()
    count += 1000
    for i in range(0, 1000):
        cur.execute(sql)

if __name__=="__main__":
    while True:
        test_insert()
        print time.strftime("%Y-%m-%d %X", time.localtime()), count
