import os
from dotenv import load_dotenv
from flask import Flask
from flask.helpers import send_from_directory

import chess
import chess.svg
from collections import OrderedDict
from operator import itemgetter
import pandas as pd
import numpy as np
import tensorflow as tf


app = Flask(__name__, static_url_path="", static_folder=".")
app.config["CORS_HEADERS"] = "Content-Type"

# Load environment variables
load_dotenv()


@app.after_request
def after_request_func(response):
    # CORS section
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


import error_handles

from routes import users

# ... and more endpoints here


@app.route("/")
def home_page():
    try:
        res = "<h1 style='position: fixed; top: 50%;  left: 50%; transform: translate(-50%, -50%);text-align:center'>FLASK API HOME<p>If you are seeing this page, Good Job. Your Flask app is ready! Add your endpoints in the /routes directory.</p></h1>"
        return res

    except Exception as e:
        print(e)


# Setting Favicon
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000, threaded=True, use_reloader=True)
