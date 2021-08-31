id1="U6e69920b85e3ae5f6b5d15e3d020029a"
import MySQLdb
class Mysql:
    def __init__(self, user_id):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = ''
        self.db = 'number'
        self.user_id = user_id

    def get_id(self):
        conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT userid,num FROM user")
        result=cursor.fetchall()
        conn.close()
        return result
    def get_max_number(self):
        conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        cursor=conn.cursor() 
        SQL = "SELECT MAX(num) FROM user"
        cursor.execute(SQL)
        res=cursor.fetchone() #取得資料
        result = res[0]
        # print(result)
        cursor.close()     #關閉 Cursor 物件
        conn.close() 
        return result
    
user_id = Mysql(id1)
res=user_id.get_id()
res1=user_id.get_max_number()
print(res1)


