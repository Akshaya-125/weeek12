from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username", "").strip()
    password = request.form.get("pwd", "")

    if not username:
        return "Username is required", 400

    if not password:
        return "Password is required", 400

    if len(password) < 6:
        return "Password must be at least 6 characters", 400

    return render_template("success.html", name=username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)