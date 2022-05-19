import sqlite3


def sqlAPI(df_bib):

    con = sqlite3.connect('example.db')
    cur = con.cursor()
    # cur.execute(
    #       ''' create table  if not exists
    #       APIModule (author, title, keywords, abstract, year, type_publication, doi)''')

    cur.execute(
        ''' create table if not exists 
        APIIEEE (rank, title, total_cities, type_publication_x, jcr_value, scimago_value, author, keywords, abstract, year, type_publication_y, doi)''')

    while True:
        cur.execute("INSERT INTO APIModule VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (df_bib.rank, df_bib.title, df_bib.total_cities, '9999', '99999', df_bib.scimago_value, df_bib.author, df_bib.keywords, df_bib.abstract, df_bib.year, df_bib.type_publication_y, df_bib.doi))
        con.commit()
        con.close()
