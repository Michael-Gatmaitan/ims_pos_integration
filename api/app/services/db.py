import mysql.connector


def ims_db():
    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="ims_db"
    )

    return db


def pos_db():
    db = mysql.connector.connect(
        host="localhost", user="root", password="", database="pos_db"
    )

    return db
