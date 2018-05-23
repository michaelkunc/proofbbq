from proofbbq import app

from config import cook, grill


@app.route("/")
def index():
    return "Hello World!"


@app.route("/cooks")
def all_cooks():
    return str([cook for cook in cook.find({}, {"_id": False})])


@app.route("/cooks/<cook_id>")
def cook_by_id(cook_id):
    return str(cook.find_one({}, {"_id": False}))


@app.route("/grills")
def all_grills():
    return str([grill for grill in grill.find({}, {"_id": False})])
