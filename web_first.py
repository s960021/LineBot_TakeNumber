from flask import Flask, render_template, Response
import cv2,os,time

#初始化 Flask app
app = Flask(__name__)
#電腦鏡頭
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)#http://56cc4c67a81e.ngrok.io/video_feed
#"C://Users//s9600//vcpkg//installed//x64-windows//tools//darknet//data//20210407_113909.jpg"
cmd = "C://Users//s9600//vcpkg//installed//x64-windows//tools//darknet"
os.chdir(cmd)   #切換路徑
print(os.getcwd())

def gen_frames(): 
   
    while True:

        success, frame = camera.read()  # read():若鏡頭有讀取到東西，會回傳True
        if not success:
            break
        else:
            #先儲存圖片
            cv2.imwrite(r'C://Users//s9600//Desktop//save_results//output.jpg', frame)
            
            frame=cv2.imread(r"C://Users//s9600//vcpkg//installed//x64-windows//tools//darknet//predictions.jpg")
            #將圖片格式轉換(編碼)成數據
            ret, buffer = cv2.imencode('.jpg', frame)   
            frame = buffer.tobytes()
            # 連接每一幀並顯示結果
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == "__main__":  #啟動Flask
    app.run(debug=True)