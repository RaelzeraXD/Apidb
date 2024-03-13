import mysql.connector
from flask import Flask ,render_template,redirect,request

mydb = mysql.connector.connect(
    host='mysqldb',
    user='user',
    password='abc123',
    database='pydb',
)
app = Flask(__name__)
mycursor = mydb.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/registration')
def registration():
    return render_template("registration.html")

@app.route('/registering', methods=['GET','POST'])
def registering():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
    command='INSERT INTO pytable (name,age,email) VALUES (%s , %s, %s)'
    mycursor.execute(command,(name,age,email))
    mydb.commit()
    return redirect('/')

@app.route('/table', methods=['GET'])
def table():
    mycursor.execute("SELECT * FROM pytable") 
    lista=mycursor.fetchall()
    return render_template('table.html',lista=lista)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
mycursor.close()
mydb.close()