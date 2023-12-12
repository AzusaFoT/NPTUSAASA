import os
import pandas as pd
from io import StringIO
import requests
import configparser

# config = configparser.ConfigParser()
# config.read('config.ini')

# Google Sheets 的 "僅供檢視" 連結
# sheet_url = config['API']['SHEET_URL_ALL']
# sheet_url_restaurant = config['API']['SHEET_URL_RESTAURANT']
# sheet_url_brunch = config['API']['SHEET_URL_BRUNCH']
# sheet_url_drink = config['API']['SHEET_URL_DRINK']
# sheet_url_snack = config['API']['SHEET_URL_SNACK']
# sheet_url_iceshop = config['API']['SHEET_URL_ICESHOP']
# sheet_url_entertainment = config['API']['SHEET_URL_ENTERTAINMENT']
# sheet_url_garage = config['API']['SHEET_URL_GARAGE']
sheet_url = os.environ['SHEET_URL_ALL']
sheet_url_restaurant = os.environ['SHEET_URL_RESTAURANT']
sheet_url_brunch = os.environ['SHEET_URL_BRUNCH']
sheet_url_drink = os.environ['SHEET_URL_DRINK']
sheet_url_snack = os.environ['SHEET_URL_SNACK']
sheet_url_iceshop = os.environ['SHEET_URL_ICESHOP']
sheet_url_entertainment = os.environ['SHEET_URL_ENTERTAINMENT']
sheet_url_garage = os.environ['SHEET_URL_GARAGE']

# 通過請求獲取 CSV 數據
response = requests.get(sheet_url_restaurant)
# 將二進制數據解碼為文字，並轉換為 DataFrame
df = pd.read_csv(StringIO(response.content.decode('utf-8-sig')))

# 指定絕對路徑以 utf-8-sig 編碼保存為 CSV 文件，並加入 BOM
# output_path = os.path.join("path", "filename.csv")
# df.to_csv(output_path, encoding='utf-8-sig', index=False)

# 得到各筆資料
# df.iloc[r, 0]是編號
# df.iloc[r, 1]是特約店名
# df.iloc[r, 2]是到期日
# df.iloc[r, 3]是特約內容
# df.iloc[r, 4]是營業時間
# df.iloc[r, 5]是地址
# df.iloc[r, 6]是連絡電話
# df.iloc[r, 7]是外送平台

# h2_value = df.iloc[0, 0]
# print(f"{h2_value}")

def get_all_data():
    # 通過請求獲取 CSV 數據
    response = requests.get(sheet_url)
    # 將二進制數據解碼為文字，並轉換為 DataFrame
    df = pd.read_csv(StringIO(response.content.decode('utf-8-sig')))
    return df
    
def get_restaurant_data():
    # 通過請求獲取 CSV 數據
    response = requests.get(sheet_url_restaurant)
    # 將二進制數據解碼為文字，並轉換為 DataFrame
    df = pd.read_csv(StringIO(response.content.decode('utf-8-sig')))
    return df

