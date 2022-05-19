import sqlite3


def sqlAPI():

    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute(
        ''' create table  if not exists 
        APIModule (author, title, keywords, abstract, year, type_publication, doi)''')

    cur.execute(
        "INSERT INTO APIModule VALUES ('2006-01-05','BUY','RHAT',100,35.14,999,999)")
    con.commit()
    con.close()
