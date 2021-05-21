from flask import Flask
from s3_interaction import list_buckets

app = Flask(__name__)

@app.route("/")
def list_endpoints():
    return "<h3>Welcome to my API</h3>" \
           "<li>/</li>" \
           "<li>/list</li>" \
           "<li>/upload</li>" \
           "<li>/delete</li>"

@app.route("/list")
def list_todos_buckets():
    resposta = list_buckets()
    return {'data': resposta['Buckets']}


