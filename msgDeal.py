from numpy import nan
from data import *
from bubbleMSGGenerator import *
import random

# get_restaurant_data() 得到 吃的 df

# 得到各筆資料
# df.iloc[r, 0]是編號
# df.iloc[r, 1]是特約店名
# df.iloc[r, 2]是到期日
# df.iloc[r, 3]是特約內容
# df.iloc[r, 4]是營業時間
# df.iloc[r, 5]是地址
# df.iloc[r, 6]是連絡電話
# df.iloc[r, 7]是外送平台

#df = get_restaurant_data()

# for i in range(次數):
#     縮排

# list1 = ['1','2','3']
# for i in list1:
#     print(i) ##這裡會直接拿取'list1裡面的東西'
df = get_all_data()
print(len(df))
# 創建 Flex Message


def find_prd_name(prd_name):
    df = get_all_data()
    exist = False
    msg = ""
    prd_name = str(prd_name)
    prd_name = prd_name.replace("查詢", "")
    prd_name = prd_name.replace("推薦", "")
    prd_name = prd_name.replace(" ", "")
    for items in range(0, len(df)):
        if (str(df.iloc[items, 1]) in prd_name) or (prd_name in str(
                df.iloc[items, 1])):
            exist = True
            open_time = df.iloc[items, 4].replace("\n", "\n\t\t")
            i = 1
            while (str(df.iloc[items, 3]) == "nan"):
                df.iloc[items, 3] = df.iloc[items - i, 3]
                i += 1
            msg += str(df.iloc[items, 1]) + "\n特約內容：" + str(
                df.iloc[items, 3]) + "\n營業時間：\n\t" + open_time + "\n地址：" + str(
                    df.iloc[items, 5]) + "\n連絡電話：" + str(df.iloc[items,
                                                                 6]) + "\n\n"
    if exist:
        return msg
    else:
        #msg = "此店家無特約"
        msg = find_prd_address(prd_name)
        return msg


def find_prd_address(prd_name):
    df = get_all_data()
    exist = False
    msg = ""
    prd_name = str(prd_name)
    prd_name = prd_name.replace("查詢", "")
    prd_name = prd_name.replace(" ", "")
    for items in range(0, len(df)):
        if (str(df.iloc[items, 5]) in prd_name) or (prd_name in str(
                df.iloc[items, 5])):
            exist = True
            open_time = df.iloc[items, 4].replace("\n", "\n\t\t")
            i = 1
            while (str(df.iloc[items, 3]) == "nan"):
                df.iloc[items, 3] = df.iloc[items - i, 3]
                i += 1
            msg += str(df.iloc[items, 1]) + "\n特約內容：" + str(
                df.iloc[items, 3]) + "\n營業時間：\n\t" + open_time + "\n地址：" + str(
                    df.iloc[items, 5]) + "\n連絡電話：" + str(df.iloc[items,
                                                                 6]) + "\n\n"
    if exist:
        return msg
    else:
        msg = "無特約店家"
        return msg


# print(find_prd_name("自由路"))


def selectRoad(prd_name):
    df = get_all_data()
    exist = False
    msg = ""
    carousel_contents = []
    prd_name = str(prd_name)
    prd_name = prd_name.replace("查詢", "")
    prd_name = prd_name.replace(" ", "")
    for items in range(0, len(df)):
        if (str(df.iloc[items, 5]) in prd_name) or (prd_name in str(
                df.iloc[items, 5])):
            exist = True
            open_time = str(df.iloc[items, 4]).replace("\n", "\n\t\t")
            if (str(df.iloc[items, 4]) == "nan"):
                open_time = "無提供，試著Google看看吧!"
            i = 1
            while (str(df.iloc[items, 3]) == "nan"):
                df.iloc[items, 3] = df.iloc[items - i, 3]
                i += 1
            # create_bubble(商店名稱,特約內容,時間,地址,電話)
            shop_msg = create_bubble(str(df.iloc[items, 1]),
                                     str(df.iloc[items, 3]), str(open_time),
                                     str(df.iloc[items, 5]),
                                     str(df.iloc[items, 6]))
            carousel_contents.append(shop_msg)
    if exist:
        msg = carousel_contents
        return msg
    else:
        msg = "無特約店家"
        return msg


def selectshop(prd_name):
    df = get_all_data()
    exist = False
    msg = ""
    carousel_contents = []
    prd_name = str(prd_name)
    prd_name = prd_name.replace("查詢", "")
    prd_name = prd_name.replace(" ", "")
    for items in range(0, len(df)):
        if (str(df.iloc[items, 1]) in prd_name) or (prd_name in str(
                df.iloc[items, 1])):
            exist = True
            i = 1
            while (str(df.iloc[items, 3]) == "nan"):
                df.iloc[items, 3] = df.iloc[items - i, 3]
                i += 1
            open_time = str(df.iloc[items, 4]).replace("\n", "\n\t")
            if (str(df.iloc[items, 4]) == "nan"):
                open_time = "無提供，試著Google看看吧!"
            # create_bubble(商店名稱,特約內容,時間,地址,電話)
            shop_msg = create_bubble(str(df.iloc[items, 1]),
                                     str(df.iloc[items, 3]), str(open_time),
                                     str(df.iloc[items, 5]),
                                     str(df.iloc[items, 6]))
            carousel_contents.append(shop_msg)
    if exist:
        msg = carousel_contents
        return msg
    else:
        msg = selectRoad(prd_name)
        return msg


# 隨機推薦特約
def recommend_prd():
    df = get_all_data()
    msg = ""
    carousel_contents = []
    for item in range(3):
        random_prd1 = random.randint(0, len(df) - 1)
        while (str(df.iloc[random_prd1, 1]) == "nan"):
            random_prd1 = random.randint(0, len(df) - 1)
        x = str(df.iloc[random_prd1, 3])
        i = 1
        while (x == "nan"):
            x = df.iloc[random_prd1 - i, 3]
            i += 1
        open_time = handle_value(str(df.iloc[random_prd1, 4]))
        shop_msg = create_bubble(str(df.iloc[random_prd1, 1]), x,
                                 str(open_time), str(df.iloc[random_prd1, 5]),
                                 str(df.iloc[random_prd1, 6]))
        carousel_contents.append(shop_msg)
    msg = carousel_contents
    return msg


def handle_value(value):
    if value != "NaN" and value != "nan":
        # 如果值不是 NaN，進行相應的處理
        return value.replace("\n", "\n\t")
    else:
        # 如果值是 NaN，返回一個默認值或進行其他特殊處理
        return '無提供，試著Google看看吧!'


print(selectshop("劉媽媽"))
#print()

# def recommend_prd():
#     df = get_all_data()
#     msg = ""
#     for items in range(0,3):
#         random_prd1=random.randint(0,len(df)-1)
#         find_prd_name(df.iloc[random_prd1, 1])
#         open_time = df.iloc[random_prd1, 4].replace("\n", "\n\t\t")
#         msg+=str(df.iloc[random_prd1, 1]) + "\n特約內容：" + str(df.iloc[random_prd1, 3]) + "\n營業時間：\n\t" + open_time + "\n地址：" + str(df.iloc[random_prd1, 5]) + "\n連絡電話：" + str(df.iloc[random_prd1,6])
#         if items != 3:
#             msg+= "\n\n"
#     return msg
