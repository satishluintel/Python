from flask import request, Flask, jsonify
app = Flask(__name__)

# dropping log4j requests
@app.route("/route", methods=['GET','POST'])
def my_i():
    if 'jndi' in str(request.headers):
        return jsonify({"Error":"Unauthorized"}), 403

if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True,debug=True)
