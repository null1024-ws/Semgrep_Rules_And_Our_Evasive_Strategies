from flask import Flask, request, make_response, escape

app = Flask(__name__)
name_key = 'name'

@app.route('/unsafe')
def unsafe():
    first_name = request.args.get(name_key, '')
    resp = "Your name is {}".format(first_name)
    return make_response(resp)