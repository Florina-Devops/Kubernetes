from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>This is a Hello World application-Florina</p>"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='1234',debug=True)