from flask import Flask,request,jsonify

app = Flask(__name__)
@app.route("/health")
def health():
    return jsonify({"Ok":"Healthy"}),200



app.run(debug=True)