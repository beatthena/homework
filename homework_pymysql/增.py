
import hashlib
import pymysql
import settings


name = input("输入用户名:")
pwd = input("输入密码:")
email=input('输入邮箱:')

try:
    coon = pymysql.Connect(**settings.peizhi)
    coon.select_db('bbs')
    cus1 = coon.cursor()
    sql = "insert into user(username,password,email) values(%s,%s,%s)"
    pwd = hashlib.sha1(pwd.encode("utf-8")).hexdigest()
    res =(name,pwd,email)
    cus1.execute(sql,res)
    coon.commit()
    cus1.close()
    coon.close()
except Exception as e:
    print(e)
else:
    print("用户创建成功")