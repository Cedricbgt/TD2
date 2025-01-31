from flask import Flask, request

app = Flask(__name__)

@app.route('/index')
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
    # Affichage non sécurisé de l'entrée utilisateur (vulnérable à XSS)
    return f"<h1>Résultats pour : {query}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
