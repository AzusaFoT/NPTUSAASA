from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)

from linebot.exceptions import (InvalidSignatureError)

from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            FlexSendMessage)
import os
from msgDeal import *
from data import *
from bubbleMSGGenerator import *

app = Flask(__name__)

token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
secret = os.environ.get("LINE_CHANNEL_SECRET")
line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)

#打招呼
greetingMSG = "HI!"


def reply_to_user(event, reply_text, i):
    if i == 1:
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=reply_text))
    elif i == 2:
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
        reply_text = selectshop(user_text)
        reply_to_user(event, reply_text, 2)
        return
    elif "推薦" in user_text:
        reply_text = create_carousel(recommend_prd())
        print(reply_text)
        reply_to_user(event, reply_text, 2)
    elif "請問" in user_text:
        reply_text = "機器人無法回覆該問題，歡迎洽學生會公關部IG將會有小編回復\n學生會公關部IG：@nptusa_prd\nhttps://www.instagram.com/nptusa_prd/"
    elif "可以簽" or "能簽" in user_text:
        reply_text = "感謝你的建議\n我只是機器人，若有想簽的特約可以到學生會公關部IG反映呦!\n學生會公關部IG：@nptusa_prd\nhttps://www.instagram.com/nptusa_prd/"

    else:
        # 如果開頭不是"HI!"，不做回應
        reply_text = "哈囉!\我是特約小祕書😉\n\n可以輸入 查詢XXX 來搜尋!\n  - 例如：- 查詢 義朵朵\n- 查詢 自由路\n或是輸入 推薦特約給我 "
        return

    # 使用函數回覆用戶
    reply_to_user(event, reply_text, 1)


app.run(host='0.0.0.0', port=8080)
