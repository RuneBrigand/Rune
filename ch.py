import hashlib
import pymysql as mdb
import base64
import requests


#f=open('/home/rune/code/cp/static/z.jpg','rb')
#a=f.read()
#f.close()
#b=hashlib.md5(a).hexdigest()
#f=open('/home/rune/code/cp/static/0.jpg','rb')
#c=f.read()
#f.close()
#e=hashlib.md5(c).hexdigest()
#aa=open(r'/home/rune/code/cp/static/z.jpg','rb')
#bb=aa.read()
#aa.close()
#encode_bb = base64.b64encode(bb)
#cc=open(r'/home/rune/code/cp/static/z.jpg','rb')
#ee=cc.read()
#cc.close()

#co='http://127.0.0.1:6625/cpp/show_page/'
#eo=hashlib.md5(co.encode()).hexdigest()
#fo='{0}'.format(eo)
#f=requests.get('https://www.baidu.com/')
#l=f.content
#f.close()




conn=mdb.connect(host='localhost',user='root',passwd='123456',db='blog')
cursor=conn.cursor()
#cc={'k':bb,'g':b}
#sql = "INSERT INTO picture (pic_value,hash_value) values ({k},{g})".format(k=b'\x87\x66\x00\x00\xff\xfe\x00',g=b.encode())
sql='''INSERT INTO customers (cus_name,cus_address,cus_phone_num) values ('zhang','aaa',11111),
       ('huang','bbb',22222),
       ('wang','ccc',33333) ;
       INSERT INTO products (vendor_id,prds_name,price,state) values (1,'pork',3,'shanghai'),
       (2,'lamb',6,'beijing'),
       (3,'steak',5,'shanghai'),
       (1,'chicken',3,'guangzhou');
       INSERT INTO carts (quantity,prds_id,cus_id) values (2,2,1),
       (4,1,1),
       (2,1,2),
       (1,4,3),
       (2,3,3);
       INSERT INTO vendors (vendor_name,vendor_address,vendor_phone_num) values ('hu','ddd',44444),
       ('liu','eee',55555),
       ('wu','fff',66666);
       
       
'''
#sql = 'insert into picture (id,pic_value, hash_value) VALUES (103, {}, "fjakdjaflk")'.format(mdb.escape_string(bb))
print(sql)
cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()






