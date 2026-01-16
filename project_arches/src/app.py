# project_arches - Cloud project: project_arches

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from project_arches!"

if __name__ == '__main__':
    app.run(debug=True)
