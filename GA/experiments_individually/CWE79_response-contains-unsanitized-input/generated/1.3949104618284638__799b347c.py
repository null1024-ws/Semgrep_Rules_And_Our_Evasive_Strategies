from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    class Data:
        def __init__(self, request):
            self.first_name = request.args.get('name', '')

    data = Data(request)
    return make_response("Your name is {}".format(data.first_name))