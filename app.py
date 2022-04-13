from flask import Flask
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB('db.json')
print(db.all())


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/<name>', methods=['POST'])
def hello(name):
    db.insert({"name": name, 'count': 9})
    return name

if __name__ == '__main__':
    app.run()
