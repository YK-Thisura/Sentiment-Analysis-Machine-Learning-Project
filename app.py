from flask import Flask, render_template # type: ignore

app = Flask(__name__)

data = dict()
reviews =['goodd rjj', 'ejfehjjkf']
positive =3
negative =6

@app.route("/")
def index():
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run()