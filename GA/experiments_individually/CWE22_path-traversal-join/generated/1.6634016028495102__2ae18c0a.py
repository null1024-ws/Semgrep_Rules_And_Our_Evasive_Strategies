import os.path
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/user_picture2")
def user_picture2():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    full_path_generator = lambda: os.path.join(base_path, filename)
    # BAD: This could still read any file on the file system
    data = open(full_path_generator(), 'rb').read()
    return data