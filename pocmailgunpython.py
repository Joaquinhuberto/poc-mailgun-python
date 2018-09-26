from flask import Flask, request

app = Flask(__name__)


@app.route('/newlead/<dealerid>', methods=['GET', 'POST'])
def pocmailgunpython(dealerid):
    content = request.get_json()
    return 'Hello World! - ' + dealerid + ' - ' + content
