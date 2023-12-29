from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    def get_name():
        return request.args.get('name', '')
    first_name = get_name()
    return make_response(f"Your name is {first_name}")