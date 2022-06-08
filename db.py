import psycopg2
from psycopg2 import sql
from config import host, user, password, db_name, port


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port,
    )
    connection.autocommit = True

    # with connection.cursor() as cursor:
    #     # cursor.execute(sql.SQL("DROP DATABASE IF EXISTS fias;"))
    #     cursor.execute(sql.SQL("CREATE DATABASE fias;"))

    with connection.cursor() as cursor:
        cursor.execute(
                """CREATE TABLE fias_region(
                ID INTEGER NOT NULL,
                REGIONCODE VARCHAR(2) NOT NULL,
                REGIONNAME VARCHAR(36),
                LEVEL integer NOT NULL,
                UPDATEDATE  date NOT NULL,
                STARTDATE  date NOT NULL,
                ENDDATE date NOT NULL,
                ISACTUAL smallint NOT NULL,
                ISACTIVE smallint NOT NULL,
                PRIMARY KEY(ID)
                );"""
            )
        print(f'[INFO]: {cursor.fetchall()}qwert')

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE fias_addres(
                ID INTEGER NOT NULL,
                ADRESSTYPE VARCHAR(16) NOT NULL,
                ADRESSNAME VARCHAR(16) NOT NULL,
                STREETCODE VARCHAR(3),
                POSTALCODE VARCHAR(6)
                );"""
        )
        print(f'[INFO]: {cursor.fetchall()}asdfg')

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE fias_addres_house(
                ID INTEGER NOT NULL,
                HOUSENUM VARCHAR(16) NOT NULL,
                HOUSECODE VARCHAR(3)
                );"""
        )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE fias_addres_kv(
                ID INTEGER NOT NULL,
                KVNUM VARCHAR(16) NOT NULL,
                KVCODE VARCHAR(3)
                );"""
        )
        print(f'[INFO]: {cursor.fetchall()}asdfg')

except Exception as _ex:
    print('[INFO] Error while working eith PostgreSQL', _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')
