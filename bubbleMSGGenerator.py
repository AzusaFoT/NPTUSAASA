import urllib.parse
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,
                            FlexSendMessage, BubbleContainer, BoxComponent,
                            TextComponent, ButtonComponent, URIAction,
                            IconComponent, CarouselContainer)


# 將氣泡放入 CarouselContainer 中
def create_carousel(a):
    return CarouselContainer(contents=[a[0], a[1], a[2]])


# 單個按鈕構建 BubbleContainer
def create_bubble(store_name, special_content, business_hours, address,
                  phone_number):
    # 將可能的特殊值替換為空字符串
    store_name = str(store_name) if store_name not in ['NaN', 'nan'
                                                       ] else '去google!'
    special_content = str(special_content) if special_content not in [
        'NaN', 'nan'
    ] else '去google!'
    business_hours = str(business_hours) if business_hours not in [
        'NaN', 'nan'
    ] else '去google!'
    address = str(address) if address not in ['NaN', 'nan'] else '去google!'
    phone_number = str(phone_number) if phone_number not in ['NaN', 'nan'
                                                             ] else '去google!'
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
