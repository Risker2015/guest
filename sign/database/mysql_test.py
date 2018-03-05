import pymysql.cursors

#Connect to the database
connection = pymysql.connect(host = '127.0.0.1',
                             user = 'root',
                             password = '123456',
                             db = 'guest',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        #create a new record
        foreign_key_off_sql = "set FOREIGN_KEY_CHECKS=0;" #关掉外键约束
        foreign_key_on_sql = "set FOREIGN_KEY_CHECKS=1;" #打开外键约束
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,create_time) VALUES ("alen",18800110001,"alen@mail.com",0,1,NOW());'

        cursor.execute(foreign_key_off_sql)
        cursor.execute(sql)
        cursor.execute(foreign_key_on_sql)

        # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit() #提交事务

    with connection.cursor() as cursor:
        #Read a single record
        sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
        cursor.execute(sql, ('18800110001',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()