from flask import Flask, render_template, request, session
import pymongo
from models.user import User
from common.database import Database
from pymongo import MongoClient
import os
app = Flask(__name__)

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client["fullstack"]
collection = database['pieces']
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            pass
            # entry_content = request.form.get("content")
            # formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            # app.db.entries.insert({"content": entry_content, "date": formatted_date})

        pieces = [ (entry["title"],entry["composer"],entry["instrument"]) for entry in app.db.entries.find({})]

        return render_template("home.html", pieces=pieces)

    return app


@app.route('/')
def hello_world():
    pieces = collection.find()
    return render_template('home.html',pieces=pieces)

@app.route('/authentication', methods=['POST','GET'])
def authenticate():
    if request.method == 'POST':
        uname = request.form['username']
        password = request.form['password']

if __name__ == '__main__':
    app.run()
