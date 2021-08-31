import requests

headers = {"Authorization":"Bearer 5eyzR/8g+f6hT5voBC06Io+mXJgJ3ldSogkSLqweTmJHVkfcu7oLXycYzNYEUVCiSplaZcntu+ludJQWIDESnFplwL6G9D30UMNTQpXpckEA9W0YQyOoh9VDNR1QMetNn/GWdJtFgL8ojPWauoYOYwdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-d35784563de58d6b2f0ebedbc2abc956', 
                       headers=headers)

print(req.text)