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
    query = request.args.get('query')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Construction de la requête SQL de manière moins évidente
    sql = "SELECT * FROM items WHERE name = '" + query + "'"
    cursor.execute(sql)  # Exécution de la requête
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

if __name__ == '__main__':
    init_db()  # Initialiser la base de données
    app.run(debug=True)  # Démarrer l'application Flask
