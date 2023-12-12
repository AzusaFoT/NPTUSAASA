import os
import pandas as pd
from io import StringIO
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
sheet_url = config['API']['SHEET_URL']
# 替換為你的 Google Sheets 的 "僅供檢視" 連結
# sheet_url = "URL"
# 通過請求獲取 CSV 數據，使用 ISO-8859-1 編碼
response = requests.get(sheet_url)
# 將二進制數據解碼為文字，並轉換為 DataFrame
df = pd.read_csv(StringIO(response.content.decode('utf-8-sig')))

# 指定絕對路徑以 utf-8-sig 編碼保存為 CSV 文件，並加入 BOM
# output_path = os.path.join("C:/Users/AzusaFoT/Desktop/teste", "output.csv")
# df.to_csv(output_path, encoding='utf-8-sig', index=False)

# 得到H2
# h2_value = df.iloc[1, 7]
# print(f"H2 是：{h2_value}")