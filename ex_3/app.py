from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip', '')
    # Vulnérabilité : Concaténation directe dans la commande
    command = f"ping -c 1 {ip}"  
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    return f"<pre>{result.stdout}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
