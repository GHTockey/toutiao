from app import create_app
from flask import jsonify

app = create_app('dev')


@app.route('/')
def route_map():
    return jsonify({'msg': 'hello world'})
