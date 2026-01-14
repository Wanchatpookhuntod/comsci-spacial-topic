### Project Flask App (project midterm)
##### 1. create folder project
- สร้าง folder project
##### 2. create virtual environment (venv)
- สร้าง virtual environment ชื่อ venv : `python -m venv venv`

- เปิดใช้ virtual environment (venv) : 
    - windows `venv\Script\activate` 
    - mac `source venv/bin/activate`

##### 3. install flask
- ติดตั้ง flask package library : `pip install flask`
##### 4. create folder project structor
- โครงสร้าง project
```
project/
├─ app.py
├─ templates/
│  └─ index.html
└─ static/
   ├─ css/style.css
   └─ js/main.js 
```
##### 5. create file app
- สร้าง `app.py`
```
# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "hello flask app."

if __name__ == "__main__":
    app.run(debug=True)
```
- run server : `flask run` หรือ `python app.py`
##### 6. create page html
- สร้างหน้า html ใน folder templates
    - index
    - login
    - registor