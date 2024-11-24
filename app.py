from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient 

app = Flask(__name__)

client = MongoClient("mongodb+srv://natashapatel2015:<db_password>@cluster0.atpjq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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
  
    return redirect(url_for('index'))
  else :
    return render_template('contact.html')

@app.route('/donate.html', methods=["GET","HEAD"])
def donate():
  return render_template('donate.html')


if __name__ == '__main__':
  app.run(debug=True)
