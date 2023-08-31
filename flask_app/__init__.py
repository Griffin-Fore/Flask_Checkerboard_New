from flask import Flask
app = Flask(__name__)
app.secret_key = 'I love pizza' # the secret key is needed to run session