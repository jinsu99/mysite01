from django.db import models

# Create your models here.
from MySQLdb import connect
from MySQLdb.cursors import DictCursor

# app.py에서 사용할 함수를 정의
# model.conn() : DB연결부분이 중복되므로 함수로 정의하기
# app.run_list() = model.findall()
# app.run_add() = model.insert()


def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')


def findbyno(no):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = 'select no, name, email, gender from user where no = %s'
        cursor.execute(sql, (no,))

        # 결과 받아오기
        result = cursor.fetchone()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return result

    except Exception as e:
        print(f'error: {e}')


def findby_email_and_password(email, password):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = 'select no, name from user where email=%s and password = %s'
        cursor.execute(sql, (email, password))

        # 결과 받아오기
        result = cursor.fetchone()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return result

    except Exception as e:
        print(f'error: {e}')


def insert(name, email, password, gender):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into user values(null, %s, %s, %s, %s, now())'
        count = cursor.execute(sql, (name, email, password, gender))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except Exception as e:
        print(f'error: {e}')


def update(name, password, gender, no):
    try:
        # DB연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = "update user set name=%s, password = %s, gender = %s where no = %s"
        count = cursor.execute(sql, (name, password, gender, no))   # 바인딩

        # DB 반영
        db.commit()

        # 자원 정리
        cursor.close()  # 커서
        db.close()      # DB연결 끊기

        # 결과 반환
        return count == 1

    except Exception as e:
        print(f'Error : {e}')  # Alt + Enter : import 단축키





















