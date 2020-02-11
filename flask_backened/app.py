from flask import Flask, render_template

app = Flask(__name__, static_folder="../react_front_end/build/static",
            template_folder="../react_front_end/build")


# @app.route("/")
# def react():
#     return render_template("index.html")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
