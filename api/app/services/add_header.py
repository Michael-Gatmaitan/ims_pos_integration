from flask import jsonify


def add_header(response):
    try:
        response = jsonify(response)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except Exception as e:
        print(f"Error in adding headers to {response}", e)
        return e
