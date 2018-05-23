from proofbbq import app

from config import cook


@app.route("/")
def index():
    return "Hello World!"


@app.route("/cooks")
def get_all_cooks():
    return str([cook for cook in cook.find({}, {"_id": False})])


@app.route("/cooks/<cook_id>")
def get_cook_by_id(cook_id):
    return str(cook.find_one({}, {"_id": False}))
