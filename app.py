from flask import Flask, render_template, request, session
import pymongo
from models.user import User
from common.database import Database
from pymongo import MongoClient
import os
app = Flask(__name__)

# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client["goodteachingmusic"]
# collection = database['pieces']
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
print(f"client uri is {os.environ.get('MONGODB_URI')}")
client = MongoClient(os.environ.get("MONGODB_URI"))
app.db = client.goodteachingmusic
col = app.db.pieces.find({})
for c in col:
    print(c["title"])


@app.route("/", methods=['POST', 'GET'])
def home():
    composer=None
    if request.method=='POST':
        composer=request.form['composer']
        pieces = [(entry["title"], entry["composer"], entry["instrument"])
                  for entry in app.db.pieces.find({'composer':composer})]
    else:
        pieces = [ (entry["title"],entry["composer"],entry["instrument"])
               for entry in app.db.pieces.find({})]
    return render_template("home.html", pieces=pieces, composer=composer)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/authentication', methods=['POST', 'GET'])
def authenticate():
    if request.method == 'POST':
        uname = request.form['username']
        password = request.form['password']



if __name__ == '__main__':
    app.run()
