from flask import Flask, render_template, request, session
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.goodteachingmusic


    @app.route("/", methods=['POST', 'GET'])
    def home():
        composer=None
        title=None
        instrument=None

        if request.method=='POST':
            print("json:")
            print(request.json)
            composer=request.form['composer'].strip()
            title = request.form['title'].strip()
            instrument = request.form['instrument'].strip()

            c=t=i=None
            qd={}
            if len(composer) > 0:
                qd['composer']=composer
            if len(title) > 0:
                qd['title']=title
            if len(instrument) > 0:
                qd['instrument']=instrument

            f=app.db.pieces.find(qd)
            pieces = [(entry["title"], entry["composer"], entry["instrument"])
                          for entry in app.db.pieces.find(qd)]
        else:
            pieces = [ (entry["title"],entry["composer"],entry["instrument"])
                   for entry in app.db.pieces.find({})]
        return render_template("home.html", pieces=pieces, composer=composer, title=title, instrument=instrument)

    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route('/authentication', methods=['POST', 'GET'])
    def authenticate():
        if request.method == 'POST':
            uname = request.form['username']
            password = request.form['password']

    return app

