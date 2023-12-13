from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)

from linebot.exceptions import (InvalidSignatureError)

from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            FlexSendMessage)
import os
from msgDeal import *
from data import *
from bubbleMSGGenerator import *
from keepAlive import keep_alive
from stringData import *

app = Flask(__name__)

token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
secret = os.environ.get("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)


def reply_to_user(event, reply_text, i):
    #一般回覆為1，會告知文字消息
    if i == 1:
        if isinstance(reply_text, str) and reply_text == "無特約店家":
            reply_text += noPRDGreetingMSG
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=reply_text))
    #特殊回覆為2，會構成用大泡泡去寫的json
    elif i == 2:
        # 假設吃到是msg == 無特約店家 轉介回去1然後return
        if isinstance(reply_text, str) and reply_text == "無特約店家":
            reply_to_user(event, reply_text, 1)
            return
        # 假設msg有東西，正常去執行
        else:
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text="Shop Information",
                                contents=reply_text))


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
    if user_text.startswith("查詢"):
        print(1)
        reply_text = create_carousel(selectshop(user_text))
        reply_to_user(event, reply_text, 2)
        return  #如果有回覆訊息就要return
    elif "推薦" in user_text:
        print(2)
        reply_text = create_carousel(recommend_prd())
        print(reply_text)
        reply_to_user(event, reply_text, 2)
        return  #如果有回覆訊息就要return
    elif "請問" in user_text:
        reply_text = cannotReplyMSG
    elif "可以簽" in user_text or "能簽" in user_text:
        reply_text = gratitudeMSG
    else:
        reply_text = greetingMSG

    # 使用函數回覆用戶
    reply_to_user(event, reply_text, 1)


app.run(host='0.0.0.0', port=8080)
