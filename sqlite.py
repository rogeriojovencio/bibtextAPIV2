import sqlite3


def sqlAPI(df):

    con = sqlite3.connect('example.db')
    cur = con.cursor()


    cur.execute(
         ''' create table if not exists
         APIIEEE (doi, title, publisher, isbn, rank)''')

    cur.execute("INSERT INTO APIIEEE VALUES (?,?,?,?,?)",
    #                  (str('doi'), str('title'), str('publisher'), str('isbn'), str('rank')))
                         (str(df.rank), str(df.title), str(df.total_cities), str('type_publication'), str('scomargo_value')))
    
    con.commit()
    
    
    cur.execute(''' CREATE TABLE IF NOT EXISTS 
                [APIIEEE2] ([ID] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,[RANK] VARCHAR(200)  NULL
                ,[TITLE] VARCHAR(200)  NULL,[TOTAL_CICITES] VARCHAR(200)  NULL, [TYPE_PUBLICATION] VARCHAR(200)  NULL
                ,[SCOMAGO_VALUE] VARCHAR(200)  NULL) ''')
    
    for row in df:
         cur.execute("INSERT INTO APIIEEE VALUES (?,?,?,?,?)",
                     (str(df.rank), str(df.title), str(df.total_cities), str('type_publication'), str('scomargo_value')))
         print(str(df.rank), str(df.title), str(df.total_cities), str('type_publication'), str('scomargo_value'))                                                                             

    con.commit()
    con.close()
