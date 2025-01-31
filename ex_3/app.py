import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    target = request.args.get('ip')
    safe_target = ''.join([c for c in target if c.isalnum() or c in ['.', '-']])  # Filtrage faible
    os.system(f'ping -c 1 {safe_target}')  # Injection de commande possible
    return "Ping sent"

if __name__ == '__main__':
    app.run(debug=True)
