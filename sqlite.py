import sqlite3

def sqlAPI():
    
    con = sqlite3.connect('example.db')    
    cur =con.cursor()
    cur.execute('''create table APIModule ()''')
