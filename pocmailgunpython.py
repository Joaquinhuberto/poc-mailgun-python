from flask import Flask
import requests

app = Flask(__name__)

@app.route('/newlead')
def pocmailgunpython(request):
    if request.method == 'POST':
        data = request.POST
        return data
    return 'Hello World!'