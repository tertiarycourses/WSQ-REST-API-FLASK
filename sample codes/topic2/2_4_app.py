from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	title = "Rendering"
	text = "Awesome day, learn a lot of stuff"
	return render_template("index3.html",title=title,text=text)

if __name__ == "__main__":
  app.run(debug=True)