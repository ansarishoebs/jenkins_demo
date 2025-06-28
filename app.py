from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
	return "Hello this is first demo code "
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
