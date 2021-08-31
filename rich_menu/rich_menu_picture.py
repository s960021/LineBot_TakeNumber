from linebot import (
    LineBotApi, WebhookHandler
)
import os

line_bot_api = LineBotApi('5eyzR/8g+f6hT5voBC06Io+mXJgJ3ldSogkSLqweTmJHVkfcu7oLXycYzNYEUVCiSplaZcntu+ludJQWIDESnFplwL6G9D30UMNTQpXpckEA9W0YQyOoh9VDNR1QMetNn/GWdJtFgL8ojPWauoYOYwdB04t89/1O/w1cDnyilFU=')

with open(r"D:\code\Project\line_reply\static\imgs\pic.png", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-d35784563de58d6b2f0ebedbc2abc956", "image/jpeg", f)