import MySQLdb


def get_id():
    id1="U6e69920b85e3ae5f6b5d15e3d020029a"
    conn=MySQLdb.connect(host="127.0.0.1",user="root", passwd="",db="number") 
    cursor=conn.cursor() 
    SQL = "SELECT userid,num FROM user"
    cursor.execute(SQL)
    result=cursor.fetchall() #取得資料
    if result ==():
        id="2"
        num="2"
    else:
        for row in result:
            num= row[1]
            id=row[0]
            if row[0] ==id:
                id = "repeat"
            break
    cursor.close()     #關閉 Cursor 物件
    conn.close() 
    return id,num
    
id,num=get_id()
print(id,num)
