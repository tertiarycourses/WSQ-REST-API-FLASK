from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	title = "Tinkering with Jinja"
	text = "Block content demo"
	return render_template("home.html",title=title,text=text)

if __name__ == "__main__":
  app.run(debug=True)