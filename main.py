from os import stat
import psycopg2
from flask import Flask, request

app = Flask(__name__)

def db_connection():    
    conn = psycopg2.connect(host="localhost", database="Flask-todo", user = "postgres",  password = "newpassword")
    return conn
    
def close_connection(curser, conn):
    curser.close()
    conn.close()

@app.route("/todo", methods = ["GET"])
def getTodos():
    conn = db_connection()
    curser = conn.cursor()

    curser.execute("SELECT * FROM todo")
    todo = curser.fetchall()

    close_connection(curser, conn)

    return {"todo": todo}

@app.route("/todo/<int:todo_id>", methods = ["GET"])
def getTodoById(todo_id):
    conn = db_connection()
    curser = conn.cursor()

    curser.execute("SELECT * FROM todo WHERE id = %s", (str(todo_id)))
    todo = curser.fetchall()

    return {"todo": todo}

@app.route("/todo", methods = ["POST"])
def addTodo():
    todo = request.form.get("todo")
    status = request.form.get("status")

    conn = db_connection()
    curser = conn.cursor()

    curser.execute("INSERT INTO todo(todo, status) values(%s, %s)", (todo, status))
    conn.commit()

    close_connection(curser, conn)

    return {"status": "success", "todo": {"todo": todo, "status": status}}

@app.route("/todo/<int:todo_id>", methods = ["DELETE"])
def deleteTodo(todo_id):
    conn = db_connection()
    curser = conn.cursor()

    curser.execute("DELETE FROM todo WHERE id = %s", (str(todo_id)))
    conn.commit()

    return {"status": "success", "message": "todo deleted"}

@app.route("/todo/<int:todo_id>", methods = ["PUT"])
def updateTodo(todo_id):
    todo = request.form.get("todo")
    status = request.form.get("status")

    conn = db_connection()
    curser = conn.cursor()

    curser.execute("UPDATE todo SET todo = %s, status = %s WHERE id = %s", (todo, status, str(todo_id)))
    conn.commit()

    return {"status": "success", "message": "todo updated"}

if __name__ == "__main__":
    app.run(debug = True)