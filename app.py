import os
from flask import Flask


# instance of Flask / Flask app and we store it in the app variable
app = Flask(__name__)


@app.route('/')
def home():
    return "TECH job in Stockholm"


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            # convert port into integer
            port=int(os.environ.get('PORT')),
            # it allows to changes to be picked up automativcelly in the browser
            debug=True)
