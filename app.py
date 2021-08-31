from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, messages
import MySQLdb   
from flask import Flask, render_template, Response
import cv2,os,time
import digit_test_newmp4 as df

app = Flask(__name__)
line_bot_api = LineBotApi('5eyzR/8g+f6hT5voBC06Io+mXJgJ3ldSogkSLqweTmJHVkfcu7oLXycYzNYEUVCiSplaZcntu+ludJQWIDESnFplwL6G9D30UMNTQpXpckEA9W0YQyOoh9VDNR1QMetNn/GWdJtFgL8ojPWauoYOYwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler("d45eb480f2885d98e95bc33d729e2ad5")
# def get_number():
#     id1="U6e69920b85e3ae5f6b5d15e3d020029a"
#     conn=MySQLdb.connect(host="127.0.0.1",user="root", passwd="",db="number") 
#     cursor=conn.cursor() 
#     SQL = "SELECT userid,num FROM user"
#     cursor.execute(SQL)
#     result=cursor.fetchall() #取得資料
#     for row in result:
#         num= row[1]
#         id=row[0]
#         if id==id1:
#             print(id,num)
#     print(id,num)
#     cursor.close()     #關閉 Cursor 物件
#     conn.close() 
#     return num

#影像
def gen_frames():  
    while True:
        success, frame = camera.read()  # read():若鏡頭有讀取到東西，會回傳True
        if not success:
            break
        else:
            #先儲存圖片
            cv2.imwrite(r'C://Users//s9600//Desktop//save_results//output.jpg', frame)
            frame=cv2.imread(r'C://Users//s9600//Desktop//save_results//output.jpg')
            #將圖片格式轉換(編碼)成數據
            ret, buffer = cv2.imencode('.jpg', frame)   
            frame = buffer.tobytes()
            # 連接每一幀並顯示結果
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# 影像
camera = cv2.VideoCapture("data/2.mp4") #"data/2.mp4"   0, cv2.CAP_DSHOW
# success, frame = camera.read()
# cv2.imwrite(r'C://Users//s9600//Desktop//save_results//output.jpg', frame)
cmd = "C://Users//s9600//vcpkg//installed//x64-windows//tools//darknet"
os.chdir(cmd)   #切換路徑
print(os.getcwd())


# 資料庫---------------------------------------------------------------------------------

def get_id(id):
    conn=MySQLdb.connect(host="127.0.0.1",user="root", passwd="",db="number") 
    cursor=conn.cursor() 
    SQL = "SELECT userid,num FROM user"
    cursor.execute(SQL)
    result=cursor.fetchall() #取得資料
    if result ==():
        id=1
        num=1
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


def get_max_number():
    conn=MySQLdb.connect(host="127.0.0.1",user="root", passwd="",db="number") 
    cursor=conn.cursor() 
    SQL = "SELECT MAX(num) FROM user"
    cursor.execute(SQL)
    res=cursor.fetchone() #取得資料
    result = res[0]
    # print(result)
    cursor.close()     #關閉 Cursor 物件
    conn.close() 
    return result


def save_number(id,num,t):
    conn=MySQLdb.connect(host="127.0.0.1",user="root", passwd="",db="number") 
    cursor=conn.cursor() 
    SQL=f"insert into user (userid,num,time) values ('{id}','{num}','{t}')"
    cursor.execute(SQL)
    conn.commit()   #操作結果寫入資料庫
    cursor.close()     #關閉 Cursor 物件
    conn.close() 


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# line
@handler.add(MessageEvent, message=TextMessage)
def number(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        if "抽號碼" in event.message.text:
            userid=event.source.user_id
            id,num=get_id(userid)
            if id =="repeat":
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=f"您已抽取過號碼牌\n您的號碼牌為:{num}")
                )
            else:
                num = get_max_number()
                if num == None:
                    num=1
                else:
                    num+=1
                now = time.localtime()
                t = int(time.strftime('%Y%m%d%H%M%S', now))
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=userid + f"\n您的號碼為:{num}號\n現在時間為:{t}")
                )
                save_number(userid,num,t)
        if "現場號碼" in event.message.text:
            text_num= df.main()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text= f"現場號碼為:{text_num}號")
            )

            
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == "__main__":
    app.run()