import sqlite3


def sqlAPI(resp):

    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute(
        ''' create table if not exists 
        APIIEEE (doi, title, publisher, isbn, rank)''')

    for row in resp:
        cur.execute("INSERT INTO APIIEEE VALUES (?,?,?,?,?)",
                    ('doi', 'df_bib.title', 'df_bib.publisher', 'df_bib.isbn', 'df_bib.rank'))

        con.commit()
        con.close()
