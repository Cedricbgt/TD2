from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Recherche</h1>
        <form action="/search" method="GET">
            <input type="text" name="query" placeholder="Entrez votre recherche">
            <button type="submit">Rechercher</button>
        </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')  # Récupère l'entrée utilisateur
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Requête SQL vulnérable à l'injection
    cursor.execute(f"SELECT * FROM items WHERE name = '{query}'")
    results = cursor.fetchall()
    conn.close()
    return f"<h1>Résultats pour : {query}</h1><p>{results}</p>"

if __name__ == '__main__':
    app.run(debug=True)
