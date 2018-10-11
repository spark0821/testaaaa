from flask import Flask , render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# Config MySQL
app.config['MYSQL_HOST'] = '35.196.78.102'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'th850413'
app.config['MYSQL_DB'] = 'LineBotdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)



app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('VDzyBBSaO8djmML0c5wgmeaMhDFUX26z9qEuQV2CO6yBAg9F4cPyHLfjOJBn1rzd+pRY3mqZuq2+RHwagF55tIIh2aas2S5Ifr0C8BQz6gnjceUiyc8i9HtD/76nyd32KiJkWMHdTdQ6qS+s7Ru+qwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('6e4f9965e8bd0e91985a1d25e8a93a42')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)
    f = open('text.txt','w')
    f.write(message)
    



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
