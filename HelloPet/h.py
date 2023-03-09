import pandas as pd

data = pd.read_excel("C:/Users/a0107/Desktop/f.xlsx")

df1 = data.where(pd.notnull(data), None)


#print(data)

import pymysql

conn = pymysql.connect(host='13.125.199.85', user='hello1234', password='qwer1234', db='hellopet')
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = 'insert into api_hospital (hosName, hosAddr, lon, lat, tel) values(%s, %s, %s, %s, %s)'


for idx in range(len(data)):
	curs.execute(sql, tuple(data.values[idx]))
conn.commit()

#종료
curs.close()
conn.close()