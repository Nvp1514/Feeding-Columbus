from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

uri = "mongodb+srv://natashapatel2015:<feedingcolumbus>@cluster0.atpjq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['FCdatabase']
collection = db['FCcollection']


@app.route('/', methods=["GET", "HEAD"])
def index():
  return render_template('index.html')

@app.route('/index.html', methods=["GET","HEAD"])
def index2():
  return render_template('index.html')

@app.route('/about.html', methods=["GET", "HEAD"])
def about():
  return render_template('about.html')

@app.route('/volunteer.html', methods=["GET","HEAD"])
def volunteer():
  return render_template('volunteer.html')

@app.route('/events.html', methods=["GET","HEAD"])
def events():
  return render_template('events.html')

@app.route('/contact.html', methods=["GET","POST"])
def contact():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    collection.insert_one({'name' : name, 'email' : email, 'phone' : phone, 'message' : message})
  
    return redirect(url_for('contact'))
  else :
    return render_template('contact.html')

@app.route('/donate.html', methods=["GET","HEAD"])
def donate():
  return render_template('donate.html')


if __name__ == '__main__':
  app.run(debug=True)
