from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    first_name = request.args.get('name', '')
    response_string = 'Your name is {}'.format(first_name)
    return make_response(response_string)