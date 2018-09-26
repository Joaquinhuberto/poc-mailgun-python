from flask import Flask
import requests

app = Flask(__name__)


@app.route('/newlead/<dealerid>', methods=['GET', 'POST'])
def pocmailgunpython(dealerid):
    content = request.json
    return 'Hello World! - ' + dealerid + ' - ' + content
