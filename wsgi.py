from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "This is my first project on openshift"

if __name__ == "__main__":
    application.run()
