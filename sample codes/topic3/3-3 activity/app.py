from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/blog/post')
def blog():
    id = request.args.get('post_id')
    return jsonify(message='Post ID = '+id), 200

if __name__ == '__main__':
    app.run(debug=True)