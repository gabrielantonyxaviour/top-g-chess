from app import app
from error_handles import forbidden
from flask import jsonify, request


@app.route("/users", methods=["POST", "GET"])
def users_controller():
    # Sample route with a method handlers and a view function
    try:
        _form = request.form
        _name = _form["name"]
        _email = _form["email"]

        if _name and _email and request.method == "POST":
            # insert record in database
            res = jsonify("success")
            res.status_code = 200
            return res

        elif request.method == "GET":
            # Get record in database
            _email = request.args["email"]
            print(_email)
            res = jsonify("users")
            res.status_code = 200
            return jsonify(users)

        else:
            return forbidden()

    except Exception as e:
        print(e)
