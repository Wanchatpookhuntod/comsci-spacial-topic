from flask import Flask, template_rendered, request, render_template

app = Flask("__name__")

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login_page():
    return render_template("login.html")

@app.route("/login_check", methods=["get", "post"])
def login_check():
    user_name = request.form.get("username")
    return user_name

if __name__ == "__main__":
    app.run(debug=True)