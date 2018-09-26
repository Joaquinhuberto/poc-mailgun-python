from flask import Flask

app = Flask(__name__)

@app.route('/newdealer/')
def pocmailgunpython(request, dealerid):
    data = None
    if request.method == 'POST':
        data = request.POST
        return data
    return 'Hello World'