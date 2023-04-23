from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # connessione al database:
    connection = sqlite3.connect('database.db')
    connection.row_factory=sqlite3.Row #in questo modo la connessione al database sarà organizzata in righe.
    posts = connection.execute('SELECT * FROM posts').fetchall() #seleziona tutte le righe all'interno della tabella post
    # fetchall() fa si che tutte le righe siano organizzate in una semplice lista python.
    connection.close()

    # ora bisogna passare la lista posts al template html.
    # è sufficiente aggiungerlo come parametro della funzione render template
    return render_template('index.html', posts=posts)
    # il primo è il parametro, il secondo è la variabile in se che contiene la lista.


@app.route('/<int:idx>/delete', methods=('POST',)) #definito un parametro in ingresso (numero intero id), secondo argomento methods con tupla di richieste
def delete(idx):
    connection = sqlite3.connect('database.db')
    connection.row_factory=sqlite3.Row #in questo modo la connessione al database sarà organizzata in righe.
    connection.execute('DELETE FROM posts WHERE id=?', (idx,))
    connection.commit()
    connection.close()
    return redirect('/')

@app.route('/create', methods=('GET', 'POST'))
def create(): #si  occuperà di gestire le richieste a tale indirizzo
    if request.method == 'POST':
        titolo = request.form['titolo']
        info = request.form['info']
        connection = sqlite3.connect('database.db')
        connection.row_factory=sqlite3.Row #in questo modo la connessione al database sarà organizzata in righe.
        connection.execute('INSERT INTO posts (titolo, info) VALUES (?, ?)', (titolo, info))
        connection.commit()
        connection.close()
        return redirect('/')
    
    return render_template('create.html')