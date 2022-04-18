from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	# return render_template("index4b.html",today=1)
  # return render_template("index4b.html",today=30)
  return render_template("index4b.html")

if __name__ == "__main__":
  app.run(debug=True)