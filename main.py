import os, mmh3, sys, requests, base64
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify({"usage": "/get?favicon=url.com/fav.ico"})

@app.route('/get')
def gethash():
    url = request.args.get('favicon') 
    req = requests.get(url, verify=False)
    favicon = base64.encodebytes(req.content)
    hash = mmh3.hash(favicon)
    query = "http.favicon.hash:" + str(hash)
    shodan = requests.get('https://api.shodan.io/shodan/host/search?key='+ os.environ.get("SHODAN_KEY") +'&query='+ query)
    result = shodan.json()
    entries = "<pre>query: " + query
    entries += "\ntotal: " + str(result["total"])
    
    if result["total"] > 0:
        entries += "\nresult:"
        for entry in result["matches"]:
            entries += "\n"
            entries += entry["ip_str"]

    return entries + "</pre>"
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

