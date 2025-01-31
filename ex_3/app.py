from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Créer une base de données SQLite et une table pour l'exemple
def init_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute("INSERT INTO items (name) VALUES ('apple'), ('banana'), ('cherry')")
    conn.commit()
    conn.close()

@app.route('/search')
def search():
    query = request.args.get('query')  # Récupère l'entrée utilisateur
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Requête SQL vulnérable à l'injection
    cursor.execute(f"SELECT * FROM items WHERE name = '{query}'")
    results = cursor.fetchall()
    conn.close()
    return str(results)  # Retourne les résultats de la requête

if __name__ == '__main__':
    init_db()  # Initialiser la base de données
    app.run(debug=True)  # Démarrer l'application Flask