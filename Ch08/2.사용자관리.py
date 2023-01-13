"""
날짜 : 2023/01/13
이름 : 장인화
내용 : 파이썬 사용자관리 프로그램 실습
"""

import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       user='root', 
                       password='1234', 
                       db='java1db', 
                       charset='utf8') 

#

while True:
        print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
        answer = 0
        

        try:
            answer = int(input('선택 : '))
        except Exception as e:
            print('다시 입력하세요.', e)
            continue

        
        if answer == 0:
            break
        elif answer == 1:
            cur = conn.cursor()   
            data = list(input('아이디, 비번, 이름, 휴대폰, 나이 순으로 입력 : ').split())
            cur = conn.cursor()
            sql = "insert into `user1` values ('%s', '%s', '%s', '%s', '%s')"
            cur.execute(sql % (data[0], data[1], data[2], data[3], data[4]))
            conn.commit()

            conn.close
            print('등록 완료...')



        elif answer == 2:
            cur = conn.cursor()
            sql = "select * from `user1`"
            cur.execute(sql)
            conn.commit()

            for row in cur.fetchall():
                print('------------')
                print('아이디 : ', row[0])
                print('비밀번호 : ', row[1])
                print('이름 : ', row[2])
                print('휴대폰 : ', row[3])
                print('나이 : ', row[4])

            print('조회 완료...')

        elif answer == 3:
            cur = conn.cursor()
            name = input('이름 검색 : ')

            sql = "select * from `user1` where `name` = '{}'"
            cur.execute(sql.format(name))
            conn.commit()


            # 데이터 출력
            for row in cur.fetchall():
                print('------------')
                print('아이디 : ', row[0])
                print('비밀번호 : ', row[1])
                print('이름 : ', row[2])
                print('휴대폰 : ', row[3])
                print('나이 : ', row[4])

            print('검색 완료...')

        elif answer == 4:
            name = input('삭제할 이름 : ')
            cur = conn.cursor()
            cur.execute("delete from `user1` where `name`='{}'".format(name))
            conn.commit()

            print('삭제완료...')
        else:
            print('0 ~ 4 중에 입력하세요.')
        

# 데이터베이스 종료
conn.close
print('프로그램 종료....')