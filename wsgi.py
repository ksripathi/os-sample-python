from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! undo changed"

if __name__ == "__main__":
    application.run()
