import pymysql

class Mysql:
    def __init__(self, user_id):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = ''
        self.db = 'testrobot'
        self.charset = 'utf8'
        self.user_id = user_id

    def check_registered(self):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        cursor = conn.cursor()
        cursor.execute(f"select id from users where id = '{self.user_id}'")
        user_sta = cursor.fetchone()
        conn.close()
        return user_sta


    def insert_basic(self,name,user_picture,phone,gender):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        cursor = conn.cursor()
        sql = f"insert into users(id,user_name,user_image_url,phone_number,gender) values('{self.user_id}','{name}','{user_picture}','{phone}','{gender}');"
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def edit_member(self,phone,name,gender):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        cursor = conn.cursor()
        # 更改手機號碼
        cursor.execute(f"UPDATE users SET phone_number='{phone}' WHERE id='{self.user_id}';")
        # 更改姓名
        cursor.execute(f"UPDATE users SET user_name='{name}' WHERE id='{self.user_id}';")
        # 更改性別
        cursor.execute(f"UPDATE users SET gender='{gender}' WHERE id='{self.user_id}';")
        conn.commit()
        conn.close()


    def set_notify(self,token):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET notify_token='{token}' WHERE id='{self.user_id}';")
        conn.commit()
        conn.close()
