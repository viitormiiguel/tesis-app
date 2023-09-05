
from flask import Flask
import flask
from flask_pymongo import PyMongo
from bson import json_util
import json
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route("/api/getImages/")
def getImages():

    todos = db.pyFeat.find()

    return json.loads(json_util.dumps(todos))

@app.route("/api/getImage/<string:todoId>")
def insert_one(todoId):
    
    todo = db.pyFeat.find_one({"_id": ObjectId(todoId)})
    
    return json.loads(json_util.dumps(todo))

if __name__ == '__main__':

    # Init mongodb
    mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/tesis-app")

    # Connect mongodb
    db = mongodb_client.db

    app.run()
