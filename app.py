from flask import Flask, render_template, request, session, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.goodteachingmusic

    @app.route("/json", methods = ["POST","GET"])
    def json():
        if request.method == 'POST':
            composer = request.form['composer'].strip()
            title = request.form['title'].strip()
            instrument = request.form['instrument'].strip()

            c = t = i = None
            qd = {}
            if len(composer) > 0:
                qd['composer'] = composer
            if len(title) > 0:
                qd['title'] = title
            if len(instrument) > 0:
                qd['instrument'] = instrument

            f = app.db.pieces.find(qd)
            pieces = [(entry["title"], entry["composer"], entry["instrument"])
                      for entry in app.db.pieces.find(qd)]

        else:
            pieces = [(entry["title"], entry["composer"], entry["instrument"])
                      for entry in app.db.pieces.find({})]
        return jsonify(pieces)

    @app.route("/", methods=['POST', 'GET'])
    @app.route("/home")
    def home():
        composer=None
        title=None
        instrument=None
        for key in request.args.keys():
            if key=="title":
                title=request.args[key]
            if key=="composer":
                composer=request.args[key]
            if key=="instrument":
                instrument=request.args[key]
        qd={}
        if title:
            qd['title']=title
        if composer:
            qd['composer']=composer
        if instrument:
            qd['instrument']=instrument

        pieces = [(entry["title"], entry["composer"], entry["instrument"])
                  for entry in app.db.pieces.find(qd)]

        if request.method=='POST':
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

        if request.headers.has_key('Content-Type'):
            if request.headers['Content-Type'] == 'application/json':
                return jsonify(pieces)
            else:
                return render_template("home.html", pieces=pieces, composer=composer, title=title,
                                       instrument=instrument)
        else:
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

