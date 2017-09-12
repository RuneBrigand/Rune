import pymysql as mdb


class Model():

    def check_order(self,customers_id:int)->list:
        result=[]
        conn = mdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='blog', charset='utf8')
        cur = conn.cursor()

        sql='''
        select * from orders where cus_id={a}
        '''.format(a=customers_id)
        cur.execute(sql)
        #print(v)
        info =cur.fetchall()
        print(info)
        if not info:
            return result
        for item in info:
            result.append({
                'name':item[2],
                'address':item[3],
                'phone_num':item[4],
                'vendor_id':item[5],
                'products_name':item[6],
                'unit_price':item[7],
                'state':item[8],
                'quantity':item[9],
                'total':item[10],

                          })

        return result

        cur.close()
        conn.close()


#f=Model()
#f.check_order(customers_id=1)