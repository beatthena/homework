import pymysql
import settings
coon = pymysql.Connect(**settings.peizhi)

#创建对象，执行sql语句
curson=coon.cursor()


#执行sql语句
curson.execute('create database bbs')

coon.select_db('bbs')



sql='''
create table user(
    uid int not null auto_increment primary key,
    username char(20) unique,
    usertype enum('0','1') default'0',
    password char(48),
    regtime date,
    email varchar(20));
'''
curson.execute(sql)



#关闭数据库
curson.close()
coon.close()
