from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('5eyzR/8g+f6hT5voBC06Io+mXJgJ3ldSogkSLqweTmJHVkfcu7oLXycYzNYEUVCiSplaZcntu+ludJQWIDESnFplwL6G9D30UMNTQpXpckEA9W0YQyOoh9VDNR1QMetNn/GWdJtFgL8ojPWauoYOYwdB04t89/1O/w1cDnyilFU=')

line_bot_api.delete_rich_menu('richmenu-d95ab4b15aaf0078683fad37aa6dfb28')