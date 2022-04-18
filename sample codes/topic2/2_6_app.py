from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	fruit = ["Apple", "Banana", "Durian","Mango"]
	return render_template("index5.html", fruit=fruit)

if __name__ == "__main__":
    app.run(debug=True)
