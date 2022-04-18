from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<title>")
def index(title):
  return render_template("index2.html",title=title,paragraph="Awesome")

if __name__ == "__main__":
  app.run()