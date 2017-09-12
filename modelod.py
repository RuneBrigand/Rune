import pymysql as mdb


class Modelad():

    def add_carts(self,customers_id:int,quant:int,products_id:int):

        conn = mdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='blog', charset='utf8')
        cur = conn.cursor()
        sql='''INSERT INTO carts (quantity,prds_id,cus_id) values ({a},{b},{d});
        '''.format(a=quant,b=products_id,d=customers_id)
        try:
            v=cur.execute(sql)
            conn.commit()

        except Exception as e:
            conn.rollback()
            v=0

        cur.close()
        conn.close()
        if v==0:
            data='error'
        else:
            data='success'
        return data


#f=Modelad()
#f.add_carts(customers_id=1,quant=11,products_id=3)