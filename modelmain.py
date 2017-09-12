import pymysql as mdb


class Modelm():

    def mainmenu(self)->list:
        result=[]
        conn = mdb.connect(host='localhost', port=3306, user='root', passwd='123456', db='blog', charset='utf8')
        cur = conn.cursor()

        sql='''
        select * from products 
        '''
        cur.execute(sql)
        #print(v)
        info =cur.fetchall()
        print(info)
        if not info:
            return result
        for item in info:
            result.append({
                'vendor_id':item[1],
                'name':item[2],
                'price':item[3],
                'state':item[4],


                          })

        return result

        cur.close()
        conn.close()