from flask import Flask , render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "HEAD"])
def index():
  return render_template('index.html')

@app.route('/about', methods=["GET", "HEAD"])
def about():
  return render_template('about.html')


if __name__ == '__main__':
  app.run()
