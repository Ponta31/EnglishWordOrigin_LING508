from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from app.services import Services


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})



def create_app():
    app = Flask(__name__)
    services = Services()

    @app.route('/')
    def doc():
        with open('app/doc.html', 'r', encoding='utf-8') as f:
            return f.read()

    @app.route('/lookup')
    def lookup_page():
        with open('web/lookup.html', 'r', encoding='utf-8') as f:
            return f.read()


    @app.route('/hello', methods=['GET'])
    def hello():
        return "Hello, World!"



    @app.route("/entries/<surface_form>", methods=['GET'])
    def lookup_entry(surface_form):
        entry = services.lookup_word(surface_form)
        if entry is None:
            return jsonify({"message": "No entry found"})
        return jsonify(entry)





    return app

if __name__ == '__main__':
    myapp = create_app()
    myapp.run(host='0.0.0.0')