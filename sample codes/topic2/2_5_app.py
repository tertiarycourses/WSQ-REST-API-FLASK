from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  #return render_template("index4.html")
	return render_template("index4.html",name="Steve")
  

if __name__ == "__main__":
  app.run(debug=True)