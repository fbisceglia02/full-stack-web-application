import sqlite3

connection = sqlite3.connect('database.db')
# la funzione sqlite.connect produrrà un oggetto che rappresenta la connessione al database

# lanciamo lo script sql scritto precedentemente:
# procediamo ad aprirlo
with open('crea_posts.sql') as f:
    connection.executescript(f.read())

# il file aperto è salvato momentaneamente nella variabile 'f'
# sull'oggetto connessione chiamiamo la funzione .executescript() per eseguire lo script di nostro interesse
# per leggere l'oggetto file f.read() come argomento della funzione executescript, che si occuperà di eseguirle

# salviamo le modifiche effettuate

connection.commit()

# chiudiamo la connessione al database
connection.close()