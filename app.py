from flask import Flask, render_template, request, session
import pymongo
from models.user import User
from common.database import Database

app = Flask(__name__)

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client["fullstack"]
collection = database['pieces']

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
