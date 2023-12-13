import random
import urllib.parse
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            FlexSendMessage, BubbleContainer, BoxComponent,
                            TextComponent, ButtonComponent, URIAction,
                            IconComponent, CarouselContainer)
from stringData import *


# 將氣泡放入 CarouselContainer 中
def create_carousel(a):
    if len(a) > 12:
        a = random.sample(a, 12)
    # 假設 a 是一個包含多個 CarouselColumn 的列表
    return CarouselContainer(contents=a)


def handle_null_values(value):
    noinfo = "無提供，試著Google看看吧!"
    nullV = [None, 'NaN', 'nan']  # 定義可能的空值
    return str(value) if value not in nullV else noinfo

# 單個按鈕構建 BubbleContainer
def create_bubble(store_name, special_content, business_hours, address,
                  phone_number):
    # 將可能的特殊值替換為空字符串
    store_name = handle_null_values(store_name)
    special_content = handle_null_values(special_content)
    business_hours = handle_null_values(business_hours)
    address = handle_null_values(address)
    phone_number = handle_null_values(phone_number)
    return BubbleContainer(
        hero={
            "type": "image",
            "url":
            "https://ugc.production.linktr.ee/zICs00Y7TLKeA8oOYrBx_1vKqxbL0ZnCLllmY?io=true&size=avatar-v1_0",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
                "type": "uri",
                "uri": "https://linktr.ee/nptusa_prd"
            }
        },
        body=BoxComponent(
            layout="vertical",
            contents=[
                TextComponent(text=store_name, weight="bold", size="xl"),
                BoxComponent(
                    layout="vertical",
                    margin="lg",
                    spacing="sm",
                    contents=[
                        BoxComponent(
                            layout="baseline",
                            spacing="sm",
                            contents=[
                                TextComponent(text="內容",
                                              color="#aaaaaa",
                                              size="sm",
                                              flex=1),
                                TextComponent(text=special_content,
                                              wrap=True,
                                              color="#666666",
                                              size="sm",
                                              flex=5)
                            ]),
                        BoxComponent(
                            layout="baseline",
                            spacing="sm",
                            contents=[
                                TextComponent(text="時間",
                                              color="#aaaaaa",
                                              size="sm",
                                              flex=1),
                                TextComponent(text=business_hours,
                                              wrap=True,
                                              color="#666666",
                                              size="sm",
                                              flex=5)
                            ]),
                        BoxComponent(
                            layout="baseline",
                            spacing="sm",
                            contents=[
                                TextComponent(text="地址",
                                              color="#aaaaaa",
                                              size="sm",
                                              flex=1),
                                TextComponent(text=address,
                                              wrap=True,
                                              color="#666666",
                                              size="sm",
                                              flex=5)
                            ]),
                        BoxComponent(
                            layout="baseline",
                            spacing="sm",
                            contents=[
                                TextComponent(text="電話",
                                              color="#aaaaaa",
                                              size="sm",
                                              flex=1),
                                TextComponent(text=phone_number,
                                              wrap=True,
                                              color="#666666",
                                              size="sm",
                                              flex=5)
                            ])
                    ])
            ]),
        footer=BoxComponent(
            layout="vertical",
            spacing="sm",
            contents=[
                ButtonComponent(
                    style="link",
                    height="sm",
                    action=URIAction(
                        label="查看更多特約商店",
                        uri=
                        "https://instagram.com/nptusa_prd?igshid=NGVhN2U2NjQ0Yg=="
                    ))
            ]))


# 使用方法
