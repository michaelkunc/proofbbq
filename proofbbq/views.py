from proofbbq import app

from config import cook

@app.route('/')
def index():
    return "Hello World!"


@app.route('/cooks')
def get_all_cooks():
    return str(cook.find_one({}, {'_id': False}))