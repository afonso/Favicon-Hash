import os, mmh3, sys, requests, base64
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def main():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"usage": "/get?favicon=url.com/fav.ico"})

@app.route('/get')
def gethash():
    url = request.args.get('favicon') 
    req = requests.get(url)
    favicon = base64.encodebytes(req.content)
    hash = mmh3.hash(favicon)
    return "http.favicon.hash:" + str(hash)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

