import pandas as pd
import pymysql

# DB 정보
host = "13.125.199.85"
user = "hello1234"
password = "qwer1234"
database = "hellopet"

# 엑셀 파일 불러오기
df = pd.read_excel("C:/Users/a0107/Desktop/p.xlsx")
df = df.where(pd.notnull(df), None)
#print(df)

# DB 연결
conn = pymysql.connect(host=host, user=user, password=password, db=database)
curs = conn.cursor(pymysql.cursors.DictCursor)

# DB insert
sql = 'INSERT INTO api_pharmacy (pharName, pharAddr, lon, lat, tel) values(%s, %s, %s, %s, %s)'

for idx in range(len(df)):
    row = df.iloc[idx]
    values = (row['pharName'], row['pharAddr'], row['lon'], row['lat'], row['tel'])
    curs.execute(sql, values)

conn.commit()

# 종료
curs.close()
conn.close()