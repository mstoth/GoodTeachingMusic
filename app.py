from flask import Flask, render_template, request, session, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import json
load_dotenv()
from models.Piece import Piece
from common.database import Database

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.goodteachingmusic
    import json
    @app.route("/json", methods = ["POST","GET"])
    def json_entry():
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


    @app.route("/load/<string:fname>")
    def load(fname=None):
        with open('static/json/'+fname) as myfile:
            data=myfile.read()

        obj=json.loads(data)
        for p in obj['values']:
            newPiece=Piece(id=p[0],title=p[1],composer=p[2],
                           genre=p[3],created_at=p[4],
                           updated_at=p[5],difficulty=p[6],
                           recording=p[7],instrument=p[8],comment=p[9],
                           sheet=p[10],approved=p[11])

            existing=app.db.pieces.find({'id':newPiece.id})
            if existing.retrieved == 0:
                app.db.pieces.insert(newPiece.json())
        pieces = [(entry["id"], entry["title"], entry["composer"], entry["instrument"])
                  for entry in app.db.pieces.find({})]
        return render_template("home.html", pieces=pieces)


    @app.route("/delete/<int:id>",methods=['GET','POST'])
    def delpiece(id=None):
        if request.method == 'POST':
            if id is not None:
                app.db.pieces.remove({'id':id})
        pieces = [(entry["id"], entry["title"], entry["composer"], entry["instrument"])
                  for entry in app.db.pieces.find({})]
        return render_template("home.html", pieces=pieces)
    @app.route("/delete/all",methods=['GET','POST'])

    def delall():
        app.db.pieces.remove({})
        pieces = [(entry["id"], entry["title"], entry["composer"], entry["instrument"])
                  for entry in app.db.pieces.find({})]
        return render_template('home.html',pieces=pieces)

    @app.route("/", methods=['POST', 'GET'])
    @app.route("/home")
    def home():
        returnType=None
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
            if key=="type":
                returnType=request.args[key]
        qd={}
        if title:
            qd['title']=title
        if composer:
            qd['composer']=composer
        if instrument:
            qd['instrument']=instrument

        pieces = [(entry["id"], entry["title"], entry["composer"], entry["instrument"])
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
            if returnType is None:
                return render_template("home.html", pieces=pieces, composer=composer, title=title, instrument=instrument)
            else:
                return jsonify(pieces)


    @app.route("/login")
    def login():
        return render_template("login.html")

    @app.route('/authentication', methods=['POST', 'GET'])
    def authenticate():
        if request.method == 'POST':
            uname = request.form['username']
            password = request.form['password']

    return app

