from app.app import app
from flask import render_template, url_for


@app.route('/')
def index():
    return render_template("season.html")


if __name__ == '__main__':
    debug = True
    app.run(debug=True)