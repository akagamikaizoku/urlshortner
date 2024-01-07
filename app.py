from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  retun 'urlshortner'


if __name__ == "__main__":
  app.run()
