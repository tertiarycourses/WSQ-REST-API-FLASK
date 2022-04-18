from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index2.html",title="Flask",paragraph="Awesome")

if __name__ == "__main__":
  app.run(debug=True)