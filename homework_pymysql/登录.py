import pymysql
import hashlib
import settings

coon = pymysql.Connect(**settings.peizhi)
coon.select_db('bbs')
cus1 = coon.cursor()
# 接收用户输入
name = input("请输入用户名:")
pwd = input("请输入密码:")
res = [name]

pwd = hashlib.sha1(pwd.encode("utf-8")).hexdigest()
# 根据用户名查询密码

sql = 'select password from user where username=%s'
cus1 = coon.cursor()
cus1.execute(sql,res)
psw = cus1.fetchall()
if psw == ():
    print("用户名错误")
elif psw[0][0] == pwd:
    print("登陆成功")
else:
    print("密码错误")
coon.commit()
cus1.close()
coon.close()