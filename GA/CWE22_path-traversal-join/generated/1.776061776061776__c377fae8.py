import os.path
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/user_picture2')
def user_picture2():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    get_path = os.path.join
    data = open(get_path(base_path, filename), 'rb').read()
    return data