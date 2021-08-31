import requests
import json

headers = {"Authorization":"Bearer 5eyzR/8g+f6hT5voBC06Io+mXJgJ3ldSogkSLqweTmJHVkfcu7oLXycYzNYEUVCiSplaZcntu+ludJQWIDESnFplwL6G9D30UMNTQpXpckEA9W0YQyOoh9VDNR1QMetNn/GWdJtFgL8ojPWauoYOYwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

#"x": 854,"y": 860, //導航
#"x": 1682,"y": 4, //聯絡店家
#"x": 0,"y": 0, //會員中心 redirect
#"x": 4,"y": 852, //聯絡我們(隱藏rich menu)
#"x": 1671,"y": 848, //店家介紹
#"x": 873,"y": 5, //維修
body = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": 'true',
  "name": "圖文選單 1",
  "chatBarText": "查看更多資訊",
  "areas": [
    {
      "bounds": {
        "x": 854,
        "y": 860,
        "width": 815,
        "height": 817
      },
      "action": {
        "type": "uri",
        "uri": "https://www.google.com/maps/dir/?api=1&destination=衡新"
      }
    },
    {
      "bounds": {
        "x": 1682,
        "y": 4,
        "width": 804,
        "height": 829
      },
      "action": {
        "type": "uri",
        "uri": "https://liff.line.me/1656344100-mbg1o4QZ"
      }
    },
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 856,
        "height": 852
      },
      "action": {
        "type": "message",
        "text": "抽號碼"
      }
    },
    {
      "bounds": {
        "x": 4,
        "y": 852,
        "width": 837,
        "height": 830
      },
      "action": {
        "type": "uri",
        "uri": "https://line.me/R/oaMessage/@527rovyb/?"
      }
    },
    {
      "bounds": {
        "x": 1671,
        "y": 848,
        "width": 819,
        "height": 830
      },
      "action": {
        "type": "uri",
        "uri": "https://liff.line.me/1656172555-jEaNgZNO"
      }
    },
    {
      "bounds": {
        "x": 873,
        "y": 5,
        "width": 796,
        "height": 842
      },
      "action": {
        "type": "message",
        "text": "現場號碼"
      }
    }
  ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)