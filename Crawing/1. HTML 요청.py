"""
날짜 : 2023/01/16
이름 : 장인화
내용 : 파이썬 HTML 요청 실습하기
"""

import requests as req

url = 'http://naver.com'

html = req.get(url).text
print(html)

 