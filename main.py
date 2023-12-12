from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)

from linebot.exceptions import (InvalidSignatureError)

from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)

import os
from msgDeal.py import *

app = Flask(__name__)

token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
secret = os.environ.get("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)

#打招呼
greetingMSG = "HI!"

def reply_to_user(event, reply_text):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply_text))


@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 接收到訊息
    user_text = event.message.text

    #這邊是可以做字串處理
    if user_text.startswith("這是不可能的"):
        reply_text = greetingMSG
    else:
        # 如果開頭不是"HI!"，不做回應
        return

    # 使用函數回覆用戶
    reply_to_user(event, reply_text)


app.run(host='0.0.0.0', port=8080)
