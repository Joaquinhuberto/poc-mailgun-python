from flask import Flask

app = Flask(__name__)

@app.route('/newlead')
def pocmailgunpython(request):
    data = None
    if request.method == 'POST':
        data = request.POST
        return data
    return 'Hello World'