from flask import (Flask, request, render_template, redirect, url_for, flash)
import json, os

app = Flask(__name__)
app.secret_key = "dev"

user_name = "Wanchat"
pass_word = "12345678"

user = {}
data = []
json_path = os.path.join(app.root_path, "static", "user.json")

def data_user(new_user, json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(new_user)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route("/")
def root():
    return render_template("index.html")
@app.route("/login")
def login_page():
    return render_template("login.html")



def check_password(json_path, user, password):
    data_user_load = ""
    with open(json_path, 'r') as f:
        data_user_load = json.load(f)
    
    for data in data_user_load:
        if data["username"] == user or data["email"] == user:
            if data["password"] == password:
                return True
    return False

@app.route("/login_check", methods=["POST"])
def login_check():
    password = (request.form.get("password") or "").strip()
    username = (request.form.get("username") or "").strip()

    if username == "" or password == "":
        flash("กรุณากรอกชื่อผู้ใช้และรหัสผ่าน")
        return redirect(url_for("login_page"))
    
    is_user = check_password(json_path, username, password)

    if is_user == False:
        flash("บัญชีผู้ใช้หรือรหัสไม่ถูกต้อง")
        return redirect(url_for("login_page"))

    return render_template("goto.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    email = (request.form.get("email") or "").strip()
    username = (request.form.get("username") or "").strip()
    password = (request.form.get("password") or "").strip()

    if email == "" or username == "" or password == "":
        return render_template("register.html")
    
    new_user = {"username": username, "email": email, "password": password}
    data_user(new_user, json_path)

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)