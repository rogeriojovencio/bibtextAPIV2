import sqlite3


def sqlAPI(resp):

    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute(
        ''' create table if not exists 
        APIIEEE (doi, title, publisher, isbn, rank)''')

    for row in resp:
        cur.execute("INSERT INTO APIIEEE VALUES (?,?,?,?,?)",
                    (str(row.doi), str(row.title), str(row.publisher), str(row.isbn), str(row.rank)))

        con.commit()
        con.close()
