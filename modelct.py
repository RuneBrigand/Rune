import pymysql as mdb


class Modelc():

    def add_orders(self,customers_id:int,products_id:int):

        conn = mdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='blog', charset='utf8')
        cur = conn.cursor()
        sql='''insert into orders(cus_id,cus_name,cus_address,cus_phone_num,vendor_id,prds_name,price,state,total,quantity)
select a.id,cus_name,cus_address,cus_phone_num,vendor_id,prds_name,price,state,quantity*price as total,quantity
from carts 
left join customers a on carts.cus_id=a.id
left join products b on carts.prds_id=b.id
WHERE a.id={d} AND b.id={f}
        '''.format(d=customers_id,f=products_id)
        try:
            v=cur.execute(sql)
            conn.commit()

        except Exception :
            conn.rollback()
            v=0

        cur.close()
        conn.close()
        if v==0:
            data='error'
        else:
            data='success'
        return data